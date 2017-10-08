#/bin/bash
#For when the OSX Hoses the Apple Store
killall storeaccountd;
killall storeassetd;
killall storedownloadd;
killall storeinappd;
rm -r ~/Library/Caches/storeaccountd;
rm -r ~/Library/Caches/storeassetd;
rm -r ~/Library/Caches/storedownloadd;
rm -r ~/Library/Caches/storeinappd
echo "\nAppStore Restarted and Caches Cleared\n"
