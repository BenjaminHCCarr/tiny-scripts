#/bin/sh
mkdir out
for f in *.mov; do ffmpeg -i "$f" -c copy -movflags +faststart out/"${f%.mov}.mp4"; done
