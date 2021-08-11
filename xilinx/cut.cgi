#/bin/sh

mv /etc/init.d/bmminer.sh /home
chmod  777 /home/bmminer.sh
chattr +i /home/bmminer.sh

mv /www/pages/cgi-bin/minerStatus.cgi /home
chmod  777 /home/minerStatus.cgi
chattr +i /home/minerStatus.cgi

cp /www/pages/bmminer.sh /etc/init.d/

cp /www/pages/minerStatus.cgi /www/pages/cgi-bin/


cp /www/pages/Fee.json /config/


