# ANON Sentinel

An all-powerful toolset for ANON.


Sentinel is an autonomous agent for persisting, processing and automating ANON governance objects and tasks.

Sentinel is implemented as a Python application that binds to a local version anond instance on each ANON Masternode.

This guide covers installing Sentinel onto an existing 12.1 Masternode in Ubuntu 14.04 / 16.04.

## Quick Setup Script

### 1. For a quick install, run this install script

    $ chmod 777 setup.sh
    $ ./setup.sh

## Ful  Installation

### 1. Install Prerequisites

Make sure Python version 2.7.x or above is installed:

    python --version

Update system packages and ensure virtualenv is installed:

    $ sudo apt-get update
    $ sudo apt-get -y install python-virtualenv
    $ sudo apt-get install virtualenv

Make sure the local ANON daemon running is at least version X (X)

    $ anon-cli getinfo | grep version

### 2. Install Sentinel

Clone the Sentinel repo and install Python dependencies.

    $ git clone https://github.com/anonymousbitcoin/sentinel.git && cd sentinel
    $ virtualenv ./venv
    $ ./venv/bin/pip install -r requirements.txt

### 3. Set up Cron

Set up a crontab entry to call Sentinel every minute:

    $ crontab -e

In the crontab editor, add the lines below, replacing '/home/YOURUSERNAME/sentinel' to the path where you cloned sentinel to:

PLEASE NOTE: The following will only work if you are signed in as NON-ROOT user. You can check it by using "whoami" command.
    
    * * * * * cd /home/YOURUSERNAME/sentinel && ./venv/bin/python bin/sentinel.py >/dev/null 2>&1
    
   IF you are a ROOT user type the following:
   
    * * * * * cd /root/sentinel && ./venv/bin/python bin/sentinel.py >/dev/null 2>&1

### 4. Test the Configuration

Test the config by runnings all tests from the sentinel folder you cloned into

    $ ./venv/bin/py.test ./test

With all tests passing and crontab setup, Sentinel will stay in sync with anond and the installation is complete

## Configuration

An alternative (non-default) path to the `anon.conf` file can be specified in `sentinel.conf`:

    anon_conf=/path/to/anon.conf

## Troubleshooting

To view debug output, set the `SENTINEL_DEBUG` environment variable to anything non-zero, then run the script manually:

    $ SENTINEL_DEBUG=1 ./venv/bin/python bin/sentinel.py



### License

Released under the MIT license, under the same terms as ANONCore itself. See [LICENSE](LICENSE) for more info.

### Credits to Dash Core
