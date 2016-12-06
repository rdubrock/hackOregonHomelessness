#!/bin/bash

sh -c 'echo "deb http://apt.postgresql.org/pub/repos/apt trusty-pgdg main" >> /etc/apt/sources.list'
wget --quiet -O - http://apt.postgresql.org/pub/repos/apt/ACCC4CF8.asc | apt-key add -
apt-get update -y
apt-get upgrade -y

#install firefox
#apt-get install -y firefox

#install postgrest, postgis, and pgadmin3
apt-get install -y postgresql-9.5-postgis-2.2 pgadmin3 >> $LOGFILE
echo 'Installing postgres'

# Install pgRouting 2.1 package
apt-get install -y postgresql-9.5-pgrouting >> $LOGFILE
echo 'Installing pgRouting'

#install python for postgres
apt-get install -y postgresql-plpython3-9.5 >> $LOGFILE
echo 'Installing Python'

apt-get install -y python-pip >> $LOGFILE
echo 'Installing python-pip'
apt-get install -y dos2unix >> $LOGFILE
echo 'Installing dos2unix'
apt-get install -y postgis >> $LOGFILE
echo 'Installing postgis'
apt-get install -y unzip >> $LOGFILE
echo 'Installing unzip'

sh -c 'echo "deb http://apt.postgresql.org/pub/repos/apt trusty-pgdg main" >> /etc/apt/sources.list'
wget --quiet -O - http://apt.postgresql.org/pub/repos/apt/ACCC4CF8.asc | apt-key add -

#cleanup
apt-get autoremove -y

pip install csvkit >> $LOGFILE

#curl https://raw.githubusercontent.com/hackoregon/hack-university-database-engineering/master/Data/Crime%20Data/crimedata.csv -o /home/vagrant/proj/crimedataraw.csv >> $LOGFILE

su postgres < /home/vagrant/proj/database_creation.sh

echo 'run this on host machine: '
echo 'vagrant plugin install vagrant-vbguest'
