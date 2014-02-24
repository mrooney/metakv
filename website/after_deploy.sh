#!/bin/bash
set -e
python manage.py syncdb --migrate --noinput | egrep -v "(Installed 0|Nothing to migrate|Loading initial data)"
python manage.py test metakv 2>&1
