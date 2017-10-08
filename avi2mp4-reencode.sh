#/bin/sh
mkdir out
for f in *.avi; do ffmpeg -i "$f" -c:v libx264 -c:a copy -aviflags +faststart out/"${f%.avi}.mp4"; done

