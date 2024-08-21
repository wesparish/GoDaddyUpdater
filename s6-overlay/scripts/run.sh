#!/bin/bash

echo "Starting GoDaddy Updater, running every 60 seconds"

while /bin/true; do
  echo /usr/bin/GoDaddyUpdater.py
  /bin/sleep 60
done
