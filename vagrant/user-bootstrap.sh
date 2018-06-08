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

sudo apt-get install swig

sudo apt-get install gcc-multilib g++-multilib

mkdir pyclustering
cd pyclustering/
git clone https://github.com/annoviko/pyclustering.git .
cd ccore
make ccore

sudo -H pip install nltk

mkdir mysql_connector
cd mysql_connector/
wget https://dev.mysql.com/get/Downloads/Connector-Python/mysql-connector-python_8.0.11-1ubuntu16.04_all.deb
sudo dpkg -i mysql-connector-python_8.0.11-1ubuntu16.04_all.deb
cd ..

sudo apt-get -y install bison build-essential cmake flex git libedit-dev libllvm3.7 llvm-3.7-dev libclang-3.7-dev python zlib1g-dev libelf-dev
git clone https://github.com/iovisor/bcc.git
mkdir bcc/build
cd bcc/build
cmake .. -DCMAKE_INSTALL_PREFIX=/usr
make
sudo make install
sudo -H pip install pyroute2

git clone https://github.com/p4pktgen/p4pktgen.git
cd p4pktgen
./tools/install.sh
sudo su p4-compiler-fuzzer

echo "source /home/vagrant/p4pktgen/my-venv/bin/activate" | tee -a ~/.bashrc
sudo ln -s p4pktgen /usr/local/bin/p4pktgen
cd ~/p4-compiler-fuzzer
mkdir input
mkdir output
cd output
mkdir errors

cd ~/p4-compiler-fuzzer/src/p4-compiler-fuzzer-tamer/src
composer install -vv

echo "export PYTHONPATH='${PYTHONPATH}:/home/vagrant/pyclustering:/home/p4-compiler-fuzzer/p4-compiler-fuzzer/src/p4fuzzclib'" | tee -a ~/.bashrc
cd ~