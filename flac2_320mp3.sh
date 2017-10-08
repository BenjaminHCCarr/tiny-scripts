#!/bin/bash
[[ $# == 0 ]] && set -- *.flac
for f; do
  avconv -i "$f" -c:a libmp3lame -b:a 320k "${f[@]/%flac/mp3}"
done
