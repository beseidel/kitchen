# git clone --single-branch --branch kevin https://github.com/beseidel/kitchen

source ~/kitchen/env/bin/activate
echo "To fix Django error, type 1 "  
echo "To install everything type 2" 
echo "To deploy Django on Apache type 3" 
echo -e "Option: \c"
read error


if [ $error == 1 ] 
then
   ~/kitchen/env/bin/pip3 install -r install.txt
elif [ $error == 2 ]
then 
   sudo apt-get update
   sudo apt-get install python3-dev build-essential libssl-dev libffi-dev libxml2-dev libxslt1-dev zlib1g-dev python3-pip -y
   sudo apt-get install libmysqlclient-dev -y
   pip install -r install.txt
else 
   sudo apt-get update
   sudo apt-get install -y apache2
   sudo ufw allow 'Apache Full'
   sudo systemctl status apache2
   sudo ufw allow 'OpenSSH'
   sudo apt-get install curl
   curl -4 icanhazip.com

   if [-e /etc/apache2/sites-enabled/000-default.conf ]
   then 
      sudo rm /etc/apache2/sites-enabled/000-default.conf
      sudo cp ~/kitchen/apache.conf /etc/apache2/sites-enabled/
      sudo service apache2 restart
fi

