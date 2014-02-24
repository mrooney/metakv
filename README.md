# Metakv Django Project #

# Pre-requisites:
* python
* pip
 * sudo easy_install pip
* [optional] virtualenv
 * pip install virtualenv

# Installation:
From the directory of the repository:

1. [optional] virtualenv --no-site-packages env && source env/bin/activate
1. pip install -r requirements.txt
1. cd website
1. ./deploy.py [starts/restarts application, performing any necessary bootstrapping]
1. open http://localhost:[port]
1. ./deploy.py stop
