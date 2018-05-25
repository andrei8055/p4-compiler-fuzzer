#!/bin/bash

set -x

apt-get update

DEBIAN_FRONTEND=noninteractive apt-get -y -o Dpkg::Options::="--force-confdef" -o Dpkg::Options::="--force-confold" upgrade

debconf-set-selections <<< 'mysql-server mysql-server/root_password password p4-compiler-fuzzer'
debconf-set-selections <<< 'mysql-server mysql-server/root_password_again password p4-compiler-fuzzer'

apt-get install -y \
  git \
  vim \
  autoconf \
  automake \
  libtool \
  curl \
  make \
  g++ \
  unzip \
  libgc-dev \
  bison \
  flex \
  libfl-dev \
  libgmp-dev \
  libboost-dev \
  libboost-iostreams-dev \
  pkg-config \
  python \
  python-scapy \
  python-ipaddr \
  cmake \
  mysql-server

echo "vagrant:p4-compiler-fuzzer" | chpasswd
echo "ubuntu:p4-compiler-fuzzer" | chpasswd

useradd -m -d /home/p4-compiler-fuzzer -s /bin/bash p4-compiler-fuzzer
echo "p4-compiler-fuzzer:p4-compiler-fuzzer" | chpasswd
echo "p4-compiler-fuzzer ALL=(ALL) NOPASSWD:ALL" > /etc/sudoers.d/99_p4-compiler-fuzzer
chmod 440 /etc/sudoers.d/99_p4-compiler-fuzzer

sed -i 's/#PasswordAuthentication yes/PasswordAuthentication no/g' /etc/ssh/sshd_config
service ssh restart

mysql -u root -pp4-compiler-fuzzer -e "CREATE DATABASE fuzzer;"
mysql -u root -pp4-compiler-fuzzer -e "GRANT ALL PRIVILEGES ON fuzzer.* TO 'p4-compiler-fuzzer'@'%' IDENTIFIED BY 'p4-compiler-fuzzer';"
mysql -u root -pp4-compiler-fuzzer -e "FLUSH PRIVILEGES;"

mysql -uroot -pp4compilerfuzzer fuzzer < /home/p4-compiler-fuzzer/p4-compiler-fuzzer/sql/init.sql

sed -i 's/.*bind-address.*/bind-address = 0.0.0.0/g' /etc/mysql/mysql.conf.d/mysqld.cnf
service mysql restart

cd ~
sudo apt-get install php7.0
sudo apt-get install php7.0-fpm
sudo apt-get install php7.0-mysql
sudo apt-get install apache2
sudo a2enmod rewrite
sudo a2enmod proxy_fcgi setenvif
sudo a2enconf php7.0-fpm
sudo service apache2 restart
sudo apt-get install composer
cd /etc/apache2/sites-available/
sudo touch p4-compiler-fuzzer-tamer.conf
sudo echo -e 'Listen 8055\n<VirtualHost *:8055>\nServerName localhost\nDocumentRoot "/home/p4-compiler-fuzzer/p4-compiler-fuzzer/src/p4-compiler-fuzzer-tamer/src/public/"\nSetEnv APPLICATION_ENV "development"\n<Directory "/home/p4-compiler-fuzzer/p4-compiler-fuzzer/src/p4-compiler-fuzzer-tamer/src/public/">\nOptions Indexes FollowSymLinks MultiViews\nAllowOverride all\nOrder Deny,Allow\nAllow from all\nRequire all granted\n</Directory>\n</VirtualHost>\n' | sudo tee p4-compiler-fuzzer-tamer.conf
sudo ln -s /etc/apache2/sites-available/p4-compiler-fuzzer-tamer.conf  /etc/apache2/sites-enabled/p4-compiler-fuzzer-tamer.conf