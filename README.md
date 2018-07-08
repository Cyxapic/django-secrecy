Django Secrecy
==============

Secrecy is a simple app which create settings structure:
- DIRS:
    - settings
    - FILES > prodacion.py; development.py
- JSON file with "secret project variables"

Quick start
-----------
1. pip install django-secrecy
2. ./generator - to create settings structure.
3. Add "django_secrecy" to your INSTALLED_APPS setting.
    INSTALLED_APPS = [
        ...
        'django_secrecy',
    ]
5. Run `python manage.py secretgs` to generate JSON file.

# Default params
- `python manage.py secrets` generate default params
- if you need extra params use `python manage.py secrets --add`.
- Params <name> allways bee UPPER.

# DEBUG=True
- generate file whithout DB params, buy default - sqlite3

# TODO
- REFACTORING :D