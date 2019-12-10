# git clone --single-branch --branch kevin https://github.com/beseidel/kitchen; cd ~/kitchen; source install.sh

echo "To install requried packages in new instance, type 2" 
echo "To deploy and run full application, type 3" 
echo -e "Option: \c"
read error


if [ $error == 2 ]
then 
   sudo apt-get update
   sudo apt-get install python3-dev build-essential libssl-dev libffi-dev libxml2-dev libxslt1-dev zlib1g-dev python3-pip -y
   sudo apt-get install libmysqlclient-dev -y
   sudo ufw enable
elif [ $error == 3 ]
then   
   HOME=~/kitchen
   sudo apt-get update
   sudo pip3 install virtualenv 
   virtualenv $HOME/env
   source $HOME/env/bin/activate
   
   python_pip=$HOME/env/bin/pip3
   $python_pip install -r install.txt
   $python_pip install django-paypal
   
   sudo apt-get update
   sudo apt-get install apache2 libapache2-mod-wsgi-py3 -y
   sudo ufw allow 'Apache Full'
   sudo ufw allow 'OpenSSH'
   sudo ufw allow '3000'
   sudo ufw allow '80'
   sudo apt-get install curl
   curl -4 icanhazip.com
   file=/etc/apache2/sites-enabled/000-default.conf
   if [ -e $file ]
   then 
      sudo rm /etc/apache2/sites-enabled/000-default.conf
   fi
   sudo cp $HOME/apache.conf /etc/apache2/sites-enabled/
   sudo service apache2 restart
   
fi

