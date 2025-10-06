

#TODO

#  [ ] Add compression scripts to this repo
#  [ ] Add fdups to install script
#  [ ] Add cron job to run fdups and compression scripts
#  [ ] Add decompression scripts to this repo with -recursive option

#  [ ] change the highlight color to bright contrast


import consolidate-files.sh





#!/usr/bin/env bash

# -------------------------------------------------------------------
# 1. Configuration – edit these values to customise the script.
# -------------------------------------------------------------------
SOURCE_DIR="./"   # <-- root directory to scan 
MIN_DEPTH=1                         # Start at 2 levels deep
MAX_DEPTH=4                         # look only 3 levels deep
#DRY_RUN=false                       # true → only echo, no real work
#DELETE_AFTER=true                   # true → delete the source dir after archiving
OUTPUT_DIR="${SOURCE_DIR}"          # where the .7z files will be written (default: same as SOURCE_DIR)
#VERBOSITY=INFO						          # DEBUG, INFO, WARN, ERROR, FATAL           # read input from stdin (pipe)
#RECURSIVITY=false                   # 

# Log file – will be created (or appended) next to SOURCE_DIR
#LOGFILE="compress.log"

# -------------------------------------------------------------------
# 2. Redirect all stdout / stderr to the log while still echoing to
#    the terminal.  `exec > >(tee -a "$LOGFILE") 2>&1` does that.
# -------------------------------------------------------------------
#echo "Starting compression script – log will be written to $LOGFILE"
#exec > >(tee -a "$LOGFILE") 2>&1

# ----------------------------------------------------------------------
# 3. Safety switches
# ----------------------------------------------------------------------
set -euo pipefail      # good safety defaults
IFS=$'\n\t'            # protect against spaces in file names

# -------------------------------------------------------------------
# 4. Find all files (depth ≤ $MAX_DEPTH) in $SOURCE_DIR.
# -------------------------------------------------------------------
echo "Searching for files ($MIN_DEPTH ≤ depth ≤ $MAX_DEPTH)..."

readarray -t FILES < <(
  find "$SOURCE_DIR" -mindepth "$MIN_DEPTH" -maxdepth "$MAX_DEPTH" -depth -type f -not -path '*@eaDir*'
)

TOTAL=${#FILES[@]}

if (( ${#FILES[@]} == 0 )); then
  echo "⚠️  No files found – nothing to hash."
  exit 0
fi

echo "Found ${#FILES[@]} files."







# -------------------------------------------------------------------
# 5. Loop over each file and hash it using sum256 – progress counter added.
# -------------------------------------------------------------------
COUNT=1   # will be printed as the *current* index
for FILE in "${FILES[@]}"; do
#  [[ "$(basename "$FILE")" == '@eaFILE' ]] && continue
  
#  BASE="$(basename "$FILE")"
#  PARENT="$(filename "$FILE")"
#  ARCHIVE="${FILE%/}.7z"   # archive lives in the same parent as the sub‑directory

#  if [ "$DRY_RUN" = true ]; then
#    echo "[${COUNT}/${TOTAL}] [DRY‑RUN] Would create: $ARCHIVE from $FILE"
#    COUNT=$((COUNT+1))
#    continue
#  fi

  echo "[${COUNT}/${TOTAL}] ✔️  Hashing \"$FILE\"  …"


#  7z a -bd -mmt -mx=9 -t7z -y "$ARCHIVE" "$FILE" >/dev/null

  echo "sha256 " $FILE

#  if [[ $? -ne 0 ]]; then        # Lookup what that means; I forgot
#    echo "❌  7z failed on $FILE – aborting."
#    exit 1
#  fi

  COUNT=$((COUNT+1))
done

echo "✅  All $TOTAL files hashed."