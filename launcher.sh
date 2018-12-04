#!/bin/sh
# launcher.sh
# navigate to home directory, then to this directory, then execute python script, then back home

cd /
cd home/pi/audio-scheduler
sudo python3 main.py 
cd / 

