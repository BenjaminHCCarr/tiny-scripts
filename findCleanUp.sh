#/bin/bash
echo "Started cleanup of `pwd` : `date`"
time find . -name .DS_Stor\* -print0 | xargs -0 rm
time find . -name \.\_\* -print0 | xargs -0 rm
time find . -empty -print0 | xargs -0 rm
echo "Removed misc. files"
echo "Start fixing all directories in `pwd` : `date`"
time find ./[A-z]* -type d -print0 | xargs -0 chmod a+rx
echo "Start fixing all files in `pwd` : `date`"
time find ./[A-z]* -type f -print0 | xargs -0 chmod a+r
echo "Start removing group/other write in `pwd` : `date`"
time find ./[A-z]* -print0 | xargs -0 chmod -R go-w
echo "Finished cleanup at: `date`"
