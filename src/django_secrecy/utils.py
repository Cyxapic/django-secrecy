import os
import json
import logging


logger = logging.getLogger('setup_log')

def get_secret(setting, BASE_DIR=BASE_DIR, PROJ_NAME=PROJ_NAME):
    SECRET_FILE = os.path.join(BASE_DIR,
                               PROJ_NAME,
                               'settings',
                               'secrets.json')
    try:
        with open(SECRET_FILE, 'r') as file:
            SECRETS = json.load(file)
    except FileNotFoundError:
        logger.warning('File not found! Check BASE_DIR or PROJ_NAME')
        return None
    return SECRETS[setting]
