#!/bin/sh

echo "Running Database Migrations"
python manage.py makemigrations
python manage.py migrate

echo "Running app1 management commands"
python manage.py sample_management_command

exec "$@"