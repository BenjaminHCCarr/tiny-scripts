#/bin/bash
time freshclam
sudo clamd
time clamdscan -iz --multiscan --fdpass -l ~benc/tmp/clamdscan_Users_`date +"%Y_%m_%d_%T"`.log /Users
