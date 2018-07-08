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
        parser.add_argument('--add', nargs=None, type=str,
            default=False,
            help='Add secret value, the NAME is always capitalized!')

    def handle(self, *args, **options):
        if not os.path.exists(self.secret_file):
            print('Please generator first!')
            exit()
        if not settings.DEBUG and not options['addparam'] \
           and not os.path.exists(self.secret_file):
            self.prod_setup()
        if options['add']:
            custom_secret = self.add_param()
            self.update_file(custom_secret)

    def prod_setup(self):
        self.db_name = input('DB NAME > ')
        self.username = input('DB USERNAME > ')
        while True:
            self.db_pass = getpass.getpass(prompt='DB PASSWORD > ')
            db_pass2 = getpass.getpass(prompt='DB PASSWORD (again) > ')
            if self.db_pass == db_pass2:
                break
            else:
                print("Passwords do not match - repeat!")
        self.create_file()

    def add_param(self):
        name = input('Type NAME of value > ')
        value = input('Type secret value > ')
        if not name or not value:
            print('No value set!')
            exit()
        return {name.upper(): value}

    def create_file(self):
        secret = {
            'NAME': self.db_name,
            'USER': self.username,
            'PASSWORD': self.db_pass,
            'SECRET_KEY': self.SECRET_KEY,
        }
        self.write_file(secret)

    def update_file(self, custom_secret):
        with open(self.secret_file, 'r') as file:
            secret = json.load(file)
        secret.update(custom_secrets)
        self.write_file(secret)

    def write_file(self, secret):
        with open(self.secret_file, 'w') as file:
            json.dump(secret, file)
        print('Файл создан')
