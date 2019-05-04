#!/bin/sh

sudo apt-get install python3 python3-dev python3-pip imagemagick sextractor libxt-dev git build-essential

sudo ln -s /usr/bin/sextractor /usr/bin/sex

sudo pip3 install scipy pandas numpy pyfits pillow

cd dep/astroasciidata
sudo  python3 setup.py install

cd ../alipy
sudo python3 setup.py install

cd ../A-Track/f2n
sudo python3 setup.py install

cd ../../