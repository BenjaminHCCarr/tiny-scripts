#/bin/bash
# usually followed by "ls" or "rm"
find . -name .DS_Store -print0|xargs -0
