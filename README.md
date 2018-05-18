Django Secrecy
==============

Secrecy is a simple Django app which generates JSON file with "secret project variables"

Quick start
-----------
1. In <ProjName>/<ProjName> create dir name 'settings'
   create file '__init__.py'
   Then create files base.py, prod.py and dev.py (for development)
2. In base.py import secrets `from django_secrecy.settings import get_secrets`
3. Add to end of the base.py - `globals().update(get_secrets(BASE_DIR))`
4. Add "secrecy" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        ...
        'django_secrecy',
    ]
5. Run `python manage.py secretgenerator` to generate JSON file.

# Default params
- `python manage.py secretgenerator` generate default params
- if you need extra params use `python manage.py secretgenerator --addparam <name>=<parametr>`.
- Params <name> allways bee UPPER.

# DEBUG=True
- generate file whithout DB params, buy default - sqlite3

# TODO
- If you need DB params - you must use:
    `python manage.py secretgenerator --adddb`
