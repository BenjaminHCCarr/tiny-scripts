#/bin/bash
# usually followed by "ls" or "rm"
find . -name \.\_\* -print0 | xargs -0
