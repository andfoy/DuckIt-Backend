#!/bin/sh

clear
echo "Deploying App...\n"
POE="main_duckit.py"

PR= echo | ps ax | grep $POE | grep -v grep | awk '{print $1}' | xargs kill > /dev/null 2>&1

chmod 777 $POE

echo "Downloading latest revision from repository...\n"
git pull

echo "\nDownloading dependencies...\n"
pip install -r requirements.txt

nohup python -u $POE > "$POE.out" 2>"$POE.err"&

echo "\nProcess PID: "
echo $!

