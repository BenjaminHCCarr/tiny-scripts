start=$PWD
for directory in *; do
  cd "$directory"
  for filename in *; do
    mv "$filename" ../"$directory - $filename"
  done
  cd "$start"
done
