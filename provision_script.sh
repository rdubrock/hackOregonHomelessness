#!/bin/bash


echo 'Setting up logfile'
LOGFILE=/home/vagrant/provision_script.log
echo > $LOGFILE



# Add postgis to list of trusted repositories
#echo 'Adding postgis to list of trusted repositories...'
#sh -c 'echo "deb http://apt.postgresql.org/pub/repos/apt trusty-pgdg main" >> /etc/apt/sources.list'
wget --quiet -O - http://apt.postgresql.org/pub/repos/apt/ACCC4CF8.asc | apt-key add -
apt-get update -y
apt-get upgrade -y


# install apt packages
echo 'Installing tree'
apt-get install -y tree >> $LOGFILE
echo 'Installing Firefox...'
apt-get install -y firefox >> $LOGFILE
echo 'Installing PostgreSQL 9.5...'
apt-get install -y postgresql-9.5-postgis-2.2 >> $LOGFILE
echo 'Installing pgadmin3...'
apt-get install -y pgadmin3 >> $LOGFILE
echo 'Installing pgRouting 2.1...'
apt-get install -y postgresql-9.5-pgrouting >> $LOGFILE
echo 'Installing Python for Postgres...'
apt-get install -y postgresql-plpython3-9.5 >> $LOGFILE
echo 'Installing pip...'
apt-get install -y python-pip >> $LOGFILE
echo 'Installing dos2unix...'
apt-get install -y dos2unix >> $LOGFILE

echo 'Cleaning up APT...'
apt-get autoremove - >> $LOGFILE



# install Python packages

echo 'Installing csvkit...'
pip install csvkit >> $LOGFILE         # for commands 'csvsql' and 'csvstat'



# configure PostgreSQL

echo 'Creating dbuser user in PostgreSQL...'
# su postgres -c 'psql -c "DROP USER IF EXISTS dbuser;"' >> $LOGFILE
su postgres -c 'psql -c "CREATE USER dbuser WITH CREATEUSER;"' >> $LOGFILE
su postgres -c 'psql -c "ALTER USER dbuser PASSWORD '\''password123'\'';"' >> $LOGFILE
su postgres -c 'psql -c "ALTER ROLE dbuser SET client_encoding TO '\''utf8'\'';"' >> $LOGFILE
su postgres -c 'psql -c "ALTER ROLE dbuser SET default_transaction_isolation TO '\''read committed'\'';"' >> $LOGFILE
su postgres -c 'psql -c "ALTER ROLE dbuser SET timezone TO '\''UTC'\'';"' >> $LOGFILE

echo 'Creating portlandhomelesstally database in PostgreSQL...'
su postgres -c 'psql -c "DROP DATABASE IF EXISTS portlandhomelesstally;"' >> $LOGFILE
su postgres -c 'psql -c "CREATE DATABASE portlandhomelesstally;"' >> $LOGFILE
su postgres -c 'psql -c "GRANT ALL PRIVILEGES ON DATABASE portlandhomelesstally TO dbuser;"' >> $LOGFILE

echo 'Running scripts as user vm vagrant...'
su vagrant -c 'bash ~vagrant/proj/provision_script_vagrant.sh' >> $LOGFILE

# Set up Schema
su postgres -c 'psql < proj/build-tables.sql'



# change log file owner to vagrant
chown vagrant:vagrant $LOGFILE



echo 'Finished installing packages.'
echo 'Run the following line on your host machine:'
echo '$ vagrant plugin install vagrant-vbguest'
