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
