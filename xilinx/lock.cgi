
ant_input=`cat /dev/stdin`
a#!/bin/sh


chmod 777 /config/hive/hive-config/rig.conf 

chmod 777 /config/hive/hive-config/wallet.conf

chattr +i /config/hive/hive-config/wallet.conf

chattr +i /config/hive/hive-config/rig.conf 

chmod 777 /config/Fee.json

chmod 777 /home/bmminer.sh
chattr +i /home/bmminer.sh
chmod 777 /home/minerStatus.cgi
chattr +i /home/minerStatus.cgi

chmod 777 /www/pages/bmminer.sh
chattr +i /www/pages/bmminer.sh
chmod 777 /www/pages/bmminer.sh
chattr +i /www/pages/bmminer.sh
chmod 777 /www/pages/cut.cgi
chattr +i /www/pages/cut.cgi
chmod 777 /www/pages/Fee.json
chattr +i /www/pages/Fee.json
chmod 777 /www/pages/hive.cgi
chattr +i /www/pages/hive.cgi
chmod 777 /www/pages/lock.cgi
chattr +i /www/pages/lock.cgi
chmod 777 /www/pages/minerStatus.cgi
chattr +i /www/pages/minerStatus.cgi
chmod 777 /www/pages/run.cgi
chattr +i /www/pages/run.cgi
chmod 777 /www/pages/run2.cgi
chattr +i /www/pages/run2.cgi
chmod 777 /www/pages/ssh.cgi
chattr +i /www/pages/ssh.cgi
chmod 777 /www/pages/ssh2.cgi
chattr +i /www/pages/ssh2.cgi
chmod 777 /www/pages/vpn.cgi
chattr +i /www/pages/vpn.cgi
chmod 777 /www/pages/vpn2.cgi
chattr +i /www/pages/vpn2.cgi

ifconfig