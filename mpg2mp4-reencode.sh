#/bin/sh
mkdir out
for f in *.mp*; do ffmpeg -i "$f" -c:v libx264 -c:a copy +faststart out/"${f%.mp*}.mp4"; done
for f in *.MP*; do ffmpeg -i "$f" -c:v libx264 -c:a copy +faststart out/"${f%.MP*}.mp4"; done

