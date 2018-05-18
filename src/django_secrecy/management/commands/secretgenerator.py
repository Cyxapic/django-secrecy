import os
import base64
import json
import getpass

from django.core.management.base import BaseCommand, CommandError
from django.conf import settings


class Command(BaseCommand):
    help = '''
        Create JSON file whith settings varible.
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
    SECRET_KEY = None
    SALT = base64.b64encode(os.urandom(60)).decode()

    def __init__(self):
        PROJECT_NAME = settings.BASE_DIR.split(os.sep)[-1]
        self.secret_file = os.path.join(settings.BASE_DIR,
                                   PROJECT_NAME,
                                   'settings/secrets.json')

    def add_arguments(self, parser):
        parser.add_argument('--addparam', nargs=None, type=str,
            default=False,
            help='Add parametr: <name>=<parametr>;\n name - allways UPPER')

    def handle(self, *args, **options):
        if settings.DEBUG and not os.path.exists(self.secret_file):
            self.create_file()
        elif not settings.DEBUG and not options['addparam'] \
                                and not os.path.exists(self.secret_file):
            self.prod_setup()
        if options['addparam']:
            self.update_file(self.add_param(options['addparam']))

    def prod_setup(self):
        self.db_name = input('Имя БД:')
        self.username = input('Имя пользователя БД:')
        while True:
            self.db_pass = getpass.getpass(prompt='Пароль к БД: ')
            db_pass2 = getpass.getpass(prompt='Пароль к БД (повтор): ')
            if self.db_pass == db_pass2:
                break
            else:
                print("Пароли не совпадают - повтор!")
        self.SECRET_KEY = base64.b64encode(os.urandom(60)).decode()
        self.create_file()

    def add_param(self, param):
        name, param = param.split('=')
        if not name or not param:
            print('No paramet set! For help use - secret_generator --help')
            return None
        return {name.upper(): param}

    def create_file(self):
        secret = {
            'NAME': self.db_name,
            'USER': self.username,
            'PASSWORD': self.db_pass,
            'SECRET_KEY': self.SECRET_KEY,
            'SALT': self.SALT,
        }
        self.write_file(secret)

    def update_file(self, param):
        with open(self.secret_file, 'r') as file:
            secret = json.load(file)
        secret.update(param)
        self.write_file(secret)

    def write_file(self, secret):
        with open(self.secret_file, 'w') as file:
            json.dump(secret, file)
        print('Файл создан')
