import os
import json
import logging


logger = logging.getLogger('setup_log')

def get_secret(BASE_DIR, setting):
    PROJECT_NAME = BASE_DIR.split(os.sep)[-1]
    SECRET_FILE = os.path.join(BASE_DIR,
                               PROJECT_NAME,
                               'settings/secrets.json')
    try:
        with open(SECRET_FILE, 'r') as file:
            SECRETS = json.load(file)
    except FileNotFoundError:
        logger.warning('File not found! Please ./generator first!')
        return None
    return SECRETS[setting]

def create_file(SETTINGS_PATH):
    secret_file = os.path.join(SETTINGS_PATH, 'secrets.json')
    secret = {
        'NAME': '',
        'USER': '',
        'PASSWORD': '',
        'SECRET_KEY': 'NOT A SECRET',
    }
    with open(secret_file, 'r') as file:
        json.dump(secret, file)
