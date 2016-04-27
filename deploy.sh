#!/bin/sh

clear
echo "Deploying App...\n"
POE="main_duckit.py"
POE2="duck_services.py"

PR= echo | ps ax | grep $POE | grep -v grep | awk '{print $1}' | xargs kill > /dev/null 2>&1
PR2= echo | ps ax | grep $POE2 | grep -v grep | awk '{print $1}' | xargs kill > /dev/null 2>&1

echo "Downloading latest revision from repository...\n"
git pull

chmod 777 $POE
chmod 777 $POE2

echo "\nDownloading dependencies...\n"
pip install -r requirements.txt

nohup python -u $POE > "$POE.out" 2>"$POE.err"&

echo "\nProcess PID: "
echo $!

nohup python -u $POE2 > "$POE2.out" 2>"$POE2.err"&

echo "\nProcess PID: "
echo $!


