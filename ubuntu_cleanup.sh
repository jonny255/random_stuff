#!/usr/bin/env bash

# Enhanced Ubuntu Cleanup Script with Safety Measures
# This script performs comprehensive system cleanup while maintaining security and robustness
# EXCLUDES: hy3dgen folder from any deletion operations

# Configuration variables
CONFIG_FILE="${HOME}/.config/ubuntu_cleanup.conf"
LOG_DIR="/var/log/system_cleanup"
LOG_FILE="${LOG_DIR}/cleanup_$(date +%Y%m%d_%H%M%S).log"
DRY_RUN=0
VERBOSE=1
TIMEOUT_DURATION=1613287246
PARALLEL_JOBS=2
MAX_RESOURCE_USAGE=50
DEFAULT_RETENTION_DAYS=10

# EXCLUSION PATTERNS - Add folders/files to protect here
EXCLUDED_PATTERNS=(
    "hy3dgen"
    "Hunyuan3D"
    ".git"
    ".venv"
    "node_modules"
    "venv"
    "env"
    ".env"
)

# Load configuration if available
if [ -f "$CONFIG_FILE" ]; then
    echo "Loading configuration from $CONFIG_FILE"
    source "$CONFIG_FILE"
fi

# Create log directory if it doesn't exist
mkdir -p "$LOG_DIR" 2>/dev/null || true

# Setup logging with rotation
exec > >(tee -a "$LOG_FILE") 2>&1

# Check for root privileges
check_root() {
    if [[ $EUID -ne 0 ]]; then
        echo "This script requires elevated privileges for some operations."
        echo "You will be prompted for your password as needed."
        HAS_ROOT=0
    else
        HAS_ROOT=1
    fi
}

# Function to check if path should be excluded
is_excluded() {
    local path=$1
    for pattern in "${EXCLUDED_PATTERNS[@]}"; do
        if [[ "$path" == *"$pattern"* ]]; then
            echo "Excluding protected path: $path (matches pattern: $pattern)"
            return 0
        fi
    done
    return 1
}

# Function to handle sudo commands
run_with_privileges() {
    if [[ $HAS_ROOT -eq 1 ]]; then
        eval "$@"
    else
        sudo "$@"
    fi
}

# Function for timeout handling with user prompts
prompt_with_timeout() {
    local prompt=$1
    local timeout=$TIMEOUT_DURATION
    local response
    
    read -t "$timeout" -p "$prompt" response || true
    
    if [ -z "$response" ]; then
        echo "Timeout reached, assuming default answer (n)"
        return 1
    fi
    
    if [[ "$response" =~ ^[Yy]$ ]]; then
        return 0
    else
        return 1
    fi
}

# Function to safely remove files with exclusion check
safe_remove() {
    local target=$1
    local force=${2:-0}
    
    # Check if target should be excluded
    if is_excluded "$target"; then
        return 0
    fi
    
    # Check if target exists
    if [ ! -e "$target" ]; then
        [ $VERBOSE -eq 1 ] && echo "Warning: $target does not exist, skipping removal"
        return 0
    fi
    
    # Check if path is too dangerous to remove
    for dangerous_path in / /bin /boot /dev /etc /lib /proc /root /sbin /sys /usr /var; do
        if [ "$target" = "$dangerous_path" ]; then
            echo "Error: Refusing to remove critical system path $target"
            return 1
        fi
    done
    
    # Safe removal
    if [ -d "$target" ] && [ ! -L "$target" ]; then
        echo "Removing contents of directory $target"
        if [ $force -eq 1 ]; then
            rm -rf "${target:?}"/* 2>/dev/null || true
        else
            rm -r "${target:?}"/* 2>/dev/null || true
        fi
    else
        echo "Removing $target"
        if [ $force -eq 1 ]; then
            rm -f "$target" 2>/dev/null || true
        else
            rm "$target" 2>/dev/null || true
        fi
    fi
    
    return $?
}

# Enhanced find command that excludes protected patterns
safe_find() {
    local base_path=$1
    shift
    local find_args=("$@")
    
    # Build exclusion arguments for find
    local exclude_args=()
    for pattern in "${EXCLUDED_PATTERNS[@]}"; do
        exclude_args+=(-not -path "*${pattern}*")
    done
    
    find "$base_path" "${exclude_args[@]}" "${find_args[@]}" 2>/dev/null || true
}

# Parse command line options
while getopts "dnvt:j:r:k:" opt; do
    case $opt in
        d|n) DRY_RUN=1 ;;
        v) VERBOSE=1 ;;
        t) TIMEOUT_DURATION=$OPTARG ;;
        j) PARALLEL_JOBS=$OPTARG ;;
        r) MAX_RESOURCE_USAGE=$OPTARG ;;
        k) DEFAULT_RETENTION_DAYS=$OPTARG ;;
        *) echo "Usage: $0 [-d|-n] [-v] [-t timeout] [-j jobs] [-r max_cpu] [-k retention_days]" >&2
           echo "  -d,-n  Dry run (show what would be done)"
           echo "  -v     Verbose output"
           echo "  -t     Timeout for user prompts in seconds (default: 60)"
           echo "  -j     Number of parallel jobs (default: 2)"
           echo "  -r     Maximum CPU percentage (default: 50)"
           echo "  -k     Retention days for logs (default: 10)"
           exit 1 ;;
    esac
done

# Progress function
total_steps=21
current_step=0

progress() {
    current_step=$((current_step + 1))
    percentage=$((current_step * 100 / total_steps))
    echo -e "\n[$current_step/$total_steps] $1"
}

# Check dependencies
check_dependencies() {
    local missing_tools=()
    
    for tool in apt-get find grep awk bc; do
        if ! command -v $tool &>/dev/null; then
            missing_tools+=("$tool")
        fi
    done
    
    if [ ${#missing_tools[@]} -gt 0 ]; then
        echo "Error: Missing required tools: ${missing_tools[*]}"
        exit 1
    fi
}

# Record initial disk space
record_disk_space() {
    echo "Initial disk space usage:"
    df -h / /home
    initial_space=$(df -h / | awk 'NR==2 {print $4}')
}

# Main execution
check_dependencies
check_root
record_disk_space

echo "Protected patterns: ${EXCLUDED_PATTERNS[*]}"
echo "Starting cleanup process..."
[ $DRY_RUN -eq 1 ] && echo "DRY RUN MODE - No changes will be made"

# Confirmation prompt
if [ $DRY_RUN -eq 0 ]; then
    if ! prompt_with_timeout "Proceed with cleanup? (y/n): "; then
        echo "Aborted."
        exit 1
    fi
fi

# 1. Update package list
progress "Updating package list"
if [ $DRY_RUN -eq 0 ]; then
    run_with_privileges apt-get update || echo "Failed to update package list"
fi

# 2. Clear user cache (with exclusions)
progress "Clearing user cache (excluding protected folders)"
if [ $DRY_RUN -eq 0 ]; then
    cache_size_before=$(du -sh ~/.cache 2>/dev/null | cut -f1)
    echo "Cache size before: $cache_size_before"
    
    # Remove cache files older than 3 days, excluding protected patterns
    safe_find ~/.cache -type f -mtime +3 -exec rm -f {} \;
    
    cache_size_after=$(du -sh ~/.cache 2>/dev/null | cut -f1)
    echo "Cache size after: $cache_size_after"
fi

# 3. Clean APT cache
progress "Cleaning APT cache"
if [ $DRY_RUN -eq 0 ]; then
    run_with_privileges apt-get clean
fi

# 4. Remove obsolete packages
progress "Removing obsolete packages"
if [ $DRY_RUN -eq 0 ]; then
    run_with_privileges apt-get autoclean
fi

# 5. Remove unused packages
progress "Removing unused packages"
if [ $DRY_RUN -eq 0 ]; then
    echo "Packages to be removed:"
    run_with_privileges apt-get autoremove -y --dry-run | grep "^Remv"
    
    if prompt_with_timeout "Remove these packages? (y/n): "; then
        run_with_privileges apt-get autoremove -y
    fi
fi

# 6. Remove old kernels
progress "Checking old kernel versions"
if [ $DRY_RUN -eq 0 ]; then
    current_kernel=$(uname -r)
    echo "Current kernel: $current_kernel"
    
    if prompt_with_timeout "Remove old kernels? (y/n): "; then
        run_with_privileges apt-get autoremove --purge -y
    fi
fi

# 7. Clean Snap packages
progress "Cleaning Snap packages"
if [ $DRY_RUN -eq 0 ] && command -v snap &> /dev/null; then
    run_with_privileges snap list --all | awk '/disabled/{print $1, $3}' | \
    while read snapname revision; do
        echo "Removing $snapname revision $revision"
        run_with_privileges snap remove "$snapname" --revision="$revision"
    done
fi

# 8. Clean Flatpak
progress "Cleaning Flatpak"
if [ $DRY_RUN -eq 0 ] && command -v flatpak &> /dev/null; then
    run_with_privileges flatpak uninstall --unused -y
fi

# 9. Clear thumbnails (with age limit)
progress "Clearing old thumbnails"
if [ $DRY_RUN -eq 0 ]; then
    safe_find ~/.cache/thumbnails -type f -mtime +30 -delete
fi

# 10. Clean journal logs
progress "Cleaning systemd journal logs"
if [ $DRY_RUN -eq 0 ] && command -v journalctl &> /dev/null; then
    run_with_privileges journalctl --vacuum-time="${DEFAULT_RETENTION_DAYS}d"
    run_with_privileges journalctl --vacuum-size=50M
fi

# 11. Clean /tmp (carefully)
progress "Cleaning /tmp directory"
if [ $DRY_RUN -eq 0 ]; then
    # Only remove files older than retention days and not in use
    run_with_privileges find /tmp -type f -atime +$DEFAULT_RETENTION_DAYS \
        -not -exec fuser -s {} \; -delete 2>/dev/null || true
fi

# 12. Clean browser caches (with exclusions)
progress "Cleaning browser caches"
if [ $DRY_RUN -eq 0 ]; then
    # Firefox
    if [ -d ~/.mozilla/firefox ]; then
        safe_find ~/.mozilla/firefox -name "*Cache*" -type d -exec rm -rf {} \; || true
    fi
    
    # Chrome/Chromium
    for browser_dir in ~/.config/google-chrome ~/.config/chromium; do
        if [ -d "$browser_dir" ]; then
            safe_find "$browser_dir" -name "Cache" -type d -exec rm -rf {} \; || true
        fi
    done
fi

# 13. Manage log files
progress "Managing log files"
if [ $DRY_RUN -eq 0 ]; then
    # Compress old logs
    run_with_privileges find /var/log -type f -name "*.log" -mtime +7 -exec gzip -9 {} \; 2>/dev/null || true
    
    # Remove very old compressed logs
    run_with_privileges find /var/log -type f -name "*.gz" -mtime +$DEFAULT_RETENTION_DAYS -delete 2>/dev/null || true
fi

# 14. Check core dumps
progress "Checking core dumps"
if [ $DRY_RUN -eq 0 ] && [ -d /var/lib/apport/coredump ]; then
    core_count=$(find /var/lib/apport/coredump -type f -name "core*" | wc -l)
    if [ $core_count -gt 0 ]; then
        echo "Found $core_count core dump files"
        if prompt_with_timeout "Delete core dumps? (y/n): "; then
            run_with_privileges find /var/lib/apport/coredump -type f -name 'core*' -delete
        fi
    fi
fi

# 15. Clean package backups
progress "Cleaning package backups"
if [ $DRY_RUN -eq 0 ]; then
    # Keep only recent backups
    run_with_privileges find /var/backups -name "dpkg.status.*" | sort -r | tail -n +6 | xargs rm -f 2>/dev/null || true
fi

# 16. Clean pip cache
progress "Cleaning pip cache"
if [ $DRY_RUN -eq 0 ] && command -v pip &> /dev/null; then
    pip cache purge 2>/dev/null || true
fi

# 17. Clean conda cache
progress "Cleaning conda cache"
if [ $DRY_RUN -eq 0 ] && command -v conda &> /dev/null; then
    conda clean --all -y 2>/dev/null || true
fi

# 18. Clean npm cache
progress "Cleaning npm cache"
if [ $DRY_RUN -eq 0 ] && [ -d ~/.npm ]; then
    # Exclude node_modules and other important npm folders
    safe_find ~/.npm/_cache -type f -mtime +7 -delete || true
fi

# 19. Localepurge - Remove unnecessary locale files
progress "Cleaning unnecessary locale files"
if [ $DRY_RUN -eq 0 ]; then
    if ! command -v localepurge &> /dev/null; then
        echo "localepurge not installed"
        if prompt_with_timeout "Install localepurge to remove unused locales? (y/n): "; then
            run_with_privileges apt-get install -y localepurge
            # Run localepurge after installation
            run_with_privileges localepurge
            echo "✓ Unnecessary locale files removed"
        fi
    else
        echo "Running localepurge..."
        run_with_privileges localepurge
        echo "✓ Unnecessary locale files removed"
    fi
fi

# 20. UCareSystem Core - All-in-one system maintenance
progress "Running system maintenance with ucaresystem-core"
if [ $DRY_RUN -eq 0 ]; then
    if ! command -v ucaresystem-core &> /dev/null; then
        echo "ucaresystem-core not installed"
        if prompt_with_timeout "Install ucaresystem-core for comprehensive maintenance? (y/n): "; then
            # Add the PPA and install
            run_with_privileges add-apt-repository -y ppa:utappia/stable
            run_with_privileges apt-get update
            run_with_privileges apt-get install -y ucaresystem-core
            # Run ucaresystem after installation
            run_with_privileges ucaresystem-core -u
            echo "✓ System maintenance completed with ucaresystem-core"
        fi
    else
        echo "Running ucaresystem-core..."
        # Run without prompts in automated mode
        run_with_privileges ucaresystem-core -u
        echo "✓ System maintenance completed"
    fi
fi

# 21. Final update
progress "Final system update"
if [ $DRY_RUN -eq 0 ]; then
    if prompt_with_timeout "Update all packages? (y/n): "; then
        run_with_privileges apt-get update && run_with_privileges apt-get upgrade -y
    fi
fi

# Show results
echo -e "\nFinal disk space usage:"
df -h / /home
final_space=$(df -h / | awk 'NR==2 {print $4}')

echo -e "\nCleanup completed!"
echo "Initial free space: $initial_space"
echo "Final free space: $final_space"
echo "Log file: $LOG_FILE"
echo "Protected patterns were excluded: ${EXCLUDED_PATTERNS[*]}"
