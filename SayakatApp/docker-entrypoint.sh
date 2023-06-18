#!/bin/bash

#while ! nc -z db 3308 ; do
#    echo "Waiting for the MySQL Server"
#    sleep 3
#done

#until nc -z -v -w30 127.0.0.1 3306
#do
#  echo "Waiting for database connection..."
#  # wait for 5 seconds before check again
#  sleep 5
#done
#
## echo "Clear entire database"
## python manage.py flush --no-input

echo "Applying database migrations..."
echo "Make migrations..."
python manage.py makemigrations
echo "Migrate..."
python manage.py migrate

exec "$@"