#!/bin/bash

srcdir="$(pwd)"
user="$(whoami)"

sudo apt-get update

sudo apt-get -y install python-virtualenv

virtualenv ./venv

./venv/bin/pip install -r requirements.txt

echo "* * * * * cd ${srcdir} && ./venv/bin/python bin/sentinel.py >/dev/null 2>&1" >> /var/spool/cron/crontabs/${user}
