#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys

"""Use the command 'python manage.py createsuperuser'
   
   python manage.py runserver --settings=webpersonal.settings 

   M-V-C model view controller
   M-V-T model view template

   Libraries needed: Django, Pillow, pylint-django, django-ckeditor 

   What you see what you get, WYSWYG, un editor muy famoso y usado en este proyecto es CKeditor  
   
   For testing the email tool, we will use 'mailtrap', to check more about this please go to https://mailtrap.io/
   """


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'webempresa.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
