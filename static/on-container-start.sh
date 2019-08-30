#!/usr/bin/env bash

# Create migrations based on django models
python manage.py makemigrations

# Migrate created migrations to database
python manage.py migrate

python manage.py collectstatic --clear --noinput # clearstatic files
python manage.py collectstatic --noinput  # collect static files

# Start gunicorn server at port 8000 and keep an eye for app code changes
# If changes occur, kill worker and start a new one
gunicorn --reload Kleos2k18.wsgi:application --bind 0.0.0.0:8000