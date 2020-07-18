# PBibli

## Installation

Requirement
* git
* python 3 (with pip and venv)
* npm (https://linuxize.com/post/how-to-install-node-js-on-ubuntu-20-04/)

Clone repository

```
git clone https://github.com/Shikoruma/PBibli.git
```

Create a python virtual environement and install requirements

```
cd PBibli
#python3 must refer to python 3.6 or higher
python3 -m venv venv
. ./venv/bin/activate
pip install -r ../requirements.txt
```

Initiate django project

```
cd pbiblisite
cp pbiblisite/local_settings.py.example pbiblisite/local_settings.py
#Edit local_settings with your needs
edit pbiblisite/local_settings.py
#Create a secret key, you can find generator on internet
mkdir ../config
edit ../config/secretkey.txt
python manage.py migrate

```

Initiate vuejs project
```
cd frontend
npm install
cp .env.local.example .env.local
#Edit .env.local with your needs
edit .env.local
mkdir ./static
npm build
```

Create first admin user. 
```
#Standard user
python manage.py createsuperuser
```

