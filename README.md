Django Secrecy
==============
-----------------
- For Django 2+
-----------------
Secrecy is a simple app which create settings structure:
- DIRS:
    - settings
    - FILES > prodacion.py; development.py
- JSON file with "secret project variables"

Quick start
-----------
1. pip install django-secrecy
2. From your project root dir `./generator` - to create settings structure.
3. Add "django_secrecy" to your INSTALLED_APPS setting.
    INSTALLED_APPS = [
        ...
        'django_secrecy',
    ]
5. Run `python manage.py secrecy` - rewrite JSON with new secrets file.

## Default params
- `python manage.py secrecy` generate default params
- if you need extra params use `python manage.py secrecy --add`.
- Params <name> allways bee UPPER.

## TODO
- REFACTORING :D
