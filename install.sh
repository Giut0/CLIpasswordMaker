#!/bin/bash
pip install -r requirements.txt
sudo cp psw.py psw
chmod a+x psw
sudo cp -r psw /usr/local/bin/ 
rm psw
echo "Completated"
exit
