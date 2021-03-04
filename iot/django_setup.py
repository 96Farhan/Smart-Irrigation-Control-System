"""
Module Name: django_setup
Descriptipn: Django project setup
"""

import django
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'iot_platform.settings')
django.setup()
