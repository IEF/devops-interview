# Python application to determine if office lights should be on or off

## Prerequisites

python3, python3-venv and python3-pip packages on debian.

Furthermore, check if NTP is enabled, and the timezone is set correctly for the Netherlands:

`sudo timedatectl set-timezone Europe/Amsterdam`
`sudo timedatectl set-ntp true`

### Creating virtual environment

`python3 -m venv lights-env`

### Install required modules

`./lights-env/bin/pip install -r requirements.txt`

### Run the script

`./lights-env/bin/python3 lights.py`
