#!/usr/bin/env bash

# -------------------------------------------------------------------
# 1. Configuration – edit these values to customise the script.
# -------------------------------------------------------------------
SOURCE_DIR="./Downloads 11,209F 125GB/Datasets"   # <-- root directory to scan 
MIN_DEPTH=1                          # Start at 2 levels deep
MAX_DEPTH=1                          # look only 3 levels deep
DRY_RUN=false                        # true → only echo, no real work
DELETE_AFTER=true                    # true → delete the source dir after archiving
OUTPUT_DIR="${SOURCE_DIR}"           # where the .7z files will be written

# Log file – will be created (or appended) next to SOURCE_DIR
LOGFILE="compress.log"

# -------------------------------------------------------------------
# 2. Redirect all stdout / stderr to the log while still echoing to
#    the terminal.  `exec > >(tee -a "$LOGFILE") 2>&1` does that.
# -------------------------------------------------------------------
echo "Starting compression script – log will be written to $LOGFILE"
exec > >(tee -a "$LOGFILE") 2>&1

# ----------------------------------------------------------------------
# 3. Safety switches
# ----------------------------------------------------------------------
set -euo pipefail      # good safety defaults
IFS=$'\n\t'            # protect against spaces in file names

# -------------------------------------------------------------------
# 4. Find all sub‑directories (depth ≤ $MAX_DEPTH) in $SOURCE_DIR.
# -------------------------------------------------------------------
echo "Searching for sub‑directories ($MIN_DEPTH ≤ depth ≤ $MAX_DEPTH)..."

readarray -t DIRS < <(
  find "$SOURCE_DIR" -mindepth "$MIN_DEPTH" -maxdepth "$MAX_DEPTH" -depth -type d -not -path '*@eaDir*'
)

TOTAL=${#DIRS[@]}

if (( ${#DIRS[@]} == 0 )); then
  echo "⚠️  No sub‑directories found – nothing to compress."
  exit 0
fi

echo "Found ${#DIRS[@]} directories."

# -------------------------------------------------------------------
# 5. Loop over each directory and compress it into its own .7z file – progress counter added.
# -------------------------------------------------------------------
COUNT=1   # will be printed as the *current* index
for DIR in "${DIRS[@]}"; do
#  [[ "$(basename "$DIR")" == '@eaDir' ]] && continue
  
  BASE="$(basename "$DIR")"
  PARENT="$(dirname "$DIR")"
  ARCHIVE="${DIR%/}.7z"   # archive lives in the same parent as the sub‑directory

  if [ "$DRY_RUN" = true ]; then
    echo "[${COUNT}/${TOTAL}] [DRY‑RUN] Would create: $ARCHIVE from $DIR"
    COUNT=$((COUNT+1))
    continue
  fi

  echo "[${COUNT}/${TOTAL}] ✔️  Compressing \"$DIR\" → \"$ARCHIVE\" …"

  # The -bd flag tells 7z to stay non‑interactive (no pause prompts).
  # -mmt gives it full CPU parallelism; -t7z specifies the 7z format.
  7z a -bd -mmt -mx=9 -t7z -y "$ARCHIVE" "$DIR" >/dev/null

  if [[ $? -ne 0 ]]; then
    echo "❌  7z failed on $DIR – aborting."
    exit 1
  fi

  if [ "$DELETE_AFTER" = true ]; then
    echo "[${COUNT}/${TOTAL}] 🗑️  Deleting source directory: $DIR"
    rm -rf "$DIR"
  fi

  COUNT=$((COUNT+1))
done

echo "✅  All $TOTAL directories processed."