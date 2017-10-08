#/bin/bash
time freshclam
sudo /usr/local/sbin/clamd
sudo time clamdscan -iz --multiscan --fdpass \
-l ~benc/tmp/clamdscan_root_$(date +"%Y_%m_%d_%T").log \
--exclude-dir='/opt/metasploit-framework/' \
--exclude-dir='/Users/benc/Code' \
/
