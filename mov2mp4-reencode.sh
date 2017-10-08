#/bin/sh
mkdir out
for f in *.mov; do ffmpeg -i "$f" -c:v libx264 -c:a copy -movflags +faststart out/"${f%.mov}.mp4"; done

