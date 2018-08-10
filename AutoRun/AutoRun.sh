#!/bin/bash

# AutoRun Service @StartUp

cd /home/cae/AutoRun/

./Detector.sh

gnome-terminal --geometry 50x50+500+100 -e  ./prompt.sh
