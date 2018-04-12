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
