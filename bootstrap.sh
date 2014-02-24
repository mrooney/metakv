#!/bin/bash
set -ex
virtualenv env
source env/bin/activate
pip install -r requirements.txt
mv manage.py website
chmod +x website/manage.py
cd website
./manage.py schemamigration metakv --initial
chmod +x before_deploy.sh after_deploy.sh
pbdeploy
cd ..
git init .
git add .
git add -f website/run/.gitignore
git commit -am "initial commit"
