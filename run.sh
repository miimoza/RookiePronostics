#!/bin/bash
python3 -m venv venv
source venv/bin/activate
pip install django
pip install requests
python manage.py runserver
