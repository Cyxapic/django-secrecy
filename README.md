Django Secrecy
==============
-----------------
- python 3.6+
- Django 2+
-----------------
Secrecy is a simple app which create settings structure:
- settings:
    - prodacion.py
    - development.py
    - secrets.json; JSON file with "secret project variables"

Quick start
-----------
1. pip install django-secrecy
2. From your project root dir `./generator <project_name>` - to create settings structure.
3. Run `python manage.py secrecy` - to rewrite JSON with new secrets variables.

## Extra params
- if you need extra params use `python manage.py secrecy --add`.
- add in settings <NEW_SECRET> = secrets.<NEW_SECRET>
- Params <name> always bee UPPER.

## From repo without development.py
- to create basic developmet.py use `./generator <project_name> --dev`
- if you don't have settings `./generator <project_name> --dev`
 same effect `./generator <project_name>`

## TODO
- REFACTORING :D
