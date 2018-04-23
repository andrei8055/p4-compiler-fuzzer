#!/bin/bash

set -x

# Bmv2
git clone https://github.com/p4lang/behavioral-model
cd behavioral-model
./install_deps.sh
./autogen.sh
./configure
make
sudo make install
cd ..

# Protobuf
git clone https://github.com/google/protobuf.git
cd protobuf
git checkout v3.0.2
./autogen.sh
./configure
make
sudo make install
sudo ldconfig
cd ..

# P4C
git clone --recursive https://github.com/p4lang/p4c
cd p4c
mkdir build
cd build
cmake ..
make -j4
sudo make install
cd ..
cd ..

mkdir mysql_connector
cd mysql_connector/
wget https://dev.mysql.com/get/Downloads/Connector-Python/mysql-connector-python_8.0.11-1ubuntu16.04_all.deb
sudo dpkg -i mysql-connector-python_8.0.11-1ubuntu16.04_all.deb

sudo su p4-compiler-fuzzer
cd ~/p4-compiler-fuzzer
mkdir input
mkdir output
cd output
mkdir errors