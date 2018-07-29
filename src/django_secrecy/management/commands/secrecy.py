import os
import base64
import json
import getpass

from django.core.management.base import BaseCommand, CommandError
from django.conf import settings


class Command(BaseCommand):
    help = '''
        Create JSON file whith secrets settings varible.
        VARIBLES - 
            if DEBUG:
                DB name > string;
                DB username > string;
                DB password > very strong password;
                SECRET_KEY;
        '''
    db_name = None
    username = None
    db_pass = None
    SECRET_KEY = base64.b64encode(os.urandom(60)).decode()

    def __init__(self):
        PROJECT_NAME = settings.BASE_DIR.split(os.sep)[-1]
        self.secret_file = os.path.join(settings.BASE_DIR,
                                        PROJECT_NAME,
                                        'settings/secrets.json')

    def add_arguments(self, parser):
        parser.add_argument(
            '--add',
            action='store_true',
            dest='add',
            help='Add secret value, the NAME is always capitalized!'
        )

    def handle(self, *args, **options):
        if not os.path.exists(self.secret_file):
            print('Please start "generator" first!')
            exit()
        if options['add']:
            self._add_param()
        else:
            self._db_setup()

    def _db_setup(self):
        self.db_name = input('DB NAME > ')
        self.username = input('DB USERNAME > ')
        while True:
            self.db_pass = getpass.getpass(prompt='DB PASSWORD > ')
            db_pass2 = getpass.getpass(prompt='DB PASSWORD (again) > ')
            if self.db_pass == db_pass2:
                break
            else:
                print("Passwords do not match - repeat!")
        self._create_secrets()

    def _add_param(self):
        name = input('Type NAME of value > ')
        value = input('Type secret value > ')
        if name and value:
            self._update_file({name.upper(): value})
        else:
            print('ERROR: No value set!')
            exit()

    def _create_secrets(self):
        secret = {
            'NAME': self.db_name,
            'USER': self.username,
            'PASSWORD': self.db_pass,
            'SECRET_KEY': self.SECRET_KEY,
        }
        self._write_file(secret)
        print('Secrets written!')

    def _update_file(self, custom_secret):
        with open(self.secret_file, 'r') as file:
            secrets = json.load(file)
        secrets.update(custom_secret)
        self._write_file(secrets)
        msg = (
            "Secrets updated!\n"
            "Don't forget add <NEW_SECRET> value in settings\n"
            "<NEW_SECRET> = get_secret('<NEW_SECRET>')\n"
            "If you have error please check first DEFAULT params\n"
            "like BASE_DIR and PROJ_NAME\n"
        )
        print(msg)

    def _write_file(self, secret):
        with open(self.secret_file, 'w') as file:
            json.dump(secret, file)
