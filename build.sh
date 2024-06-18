#!/usr/bin/env bash
# exit on error
set -o errexit

pip install -r unbook/requirements.txt

python unbook/manage.py collectstatic --no-input
python unbook/manage.py migrate