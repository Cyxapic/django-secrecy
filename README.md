Django Secrecy
==============
-----------------
- python 3.6+
- Django 2+
-----------------
Secrecy is a simple app which create settings structure:
- settings:
    - prodacion.py
    - development.py (too .gitignore)
    - secrets.json; JSON file with "secret project variables"

Quick start
-----------
1. pip install django-secrecy
2. From your project root dir `./generator` - to create settings structure.
3. Run `python manage.py secrecy` - rewrite JSON with new secrets file.

## Extra params
- if you need extra params use `python manage.py secrecy --add`.
- add in settings <NEW_SECRET> = get_secret('<NEW_SECRET>', BASE_DIR, PROJ_NAME)
- Params <name> allways bee UPPER.

## TODO
- REFACTORING :D
