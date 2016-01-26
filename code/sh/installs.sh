#!/bin/bash
apt-get update
apt-get upgrade
apt-get install emacs
apt-get install cmake
apt-get install python-dev
apt-get install libopencv-dev
apt-get install python-opencv
apt-get install numpy
apt-get install scipy
apt-get install git
apt-get install python-picamera
apt-get install python-smbus
apt-get install libi2c-dev
apt-get install apache2 php5 libapache2-mod-php5

wget http://www.airspayce.com/mikem/bcm2835/bcm2835-1.49.tar.gz
tar -xvzf bcm2835-1.49.tar.gz
cd bcm2835-1.49
./configure
make
make install
cd ~/
