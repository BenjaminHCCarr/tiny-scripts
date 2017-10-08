#/bin/bash
# usually followed by "ls" or "rm"
find . -empty -print0 | xargs -0
