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
apt-get install libav-tools
wget ???bcm2835-1.46.tar.gz
tar -xvzf bcm2835-1.46.tar.gz
cd bcm2835-1.46
./configure
make
make install
cd ~/

git clone https://github.com/joaquincasanova/cvusda.git

git clone https://github.com/silvanmelchior/RPi_Cam_Web_Interface.git
cd RPi_Cam_Web_Interface
chmod u+x *.sh
