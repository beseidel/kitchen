

echo -e "To fix Django error, type '1', to install everything type '2' : \c" 
read error


if [ $error == 1 ] 
then
   pip install -r install.txt
elif [ $error == 2 ]
then 
   sudo apt-get update
   sudo apt-get install python3-dev build-essential libssl-dev libffi-dev libxml2-dev libxslt1-dev zlib1g-dev python3-pip -y
   sudo apt-get install libmysqlclient-dev -y
else
   echo "Exiting now ..."
   sleep 2
fi