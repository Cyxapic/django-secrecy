import os
import json
import logging


logger = logging.getLogger('setup_log')

def get_secrets(BASE_DIR):
    PROJECT_NAME = BASE_DIR.split(os.sep)[-1]
    SECRET_FILE = os.path.join(BASE_DIR,
                               PROJECT_NAME,
                               'settings/secrets.json')
    try:
        with open(SECRET_FILE, 'r') as file:
            SECRETS = json.load(file)
    except FileNotFoundError:
        logger.warning('File not found, create empty default settings file')
        print('Please use python manage.py secretgenerator')
        SECRETS = {
                'NAME': None,
                'USER': None,
                'PASSWORD': None,
                'SECRET_KEY': '123456',
            }
    return SECRETS