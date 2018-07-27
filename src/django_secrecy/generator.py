import os
import sys
import shutil
import argparse
import json


class Generator:

    _check = lambda self, x: os.path.exists(x)

    def __init__(self):
        self.BASE_DIR, self.SETTINGS_PATH, self.secret_file = self._get_path()

    def _get_path(self):
        parser = argparse.ArgumentParser()
        parser.add_argument("project_name", help="Django project name")
        args = parser.parse_args()
        project_name = args.project_name
        BASE_DIR = os.path.join(os.environ['VIRTUAL_ENV'], project_name)
        base_dir_settings = os.path.join(BASE_DIR, project_name)
        settings_path = os.path.join(base_dir_settings, 'settings')
        secret_file = os.path.join(settings_path, 'secrets.json')
        return base_dir_settings, settings_path, secret_file

    def _create_settings(self):
        if self._check(self.SETTINGS_PATH):
            return False
        os.mkdir(self.SETTINGS_PATH)
        TPL = os.path.dirname(os.path.abspath(__file__))
        TPL = os.path.join(TPL, 'tpl')
        settings_files = [os.path.join(TPL, file) for file in os.listdir(TPL)
                                                  if file != '__pycache__']
        for file in settings_files:
            try:
                shutil.copy(file, self.SETTINGS_PATH)
            except FileNotFoundError:
                print(f'Error >{file}')
        # delete default settings file
        try:
            os.remove(os.path.join(self.BASE_DIR, 'settings.py'))
        except FileNotFoundError:
            print('*** File "settings.py" already deleted! ***')
        return True

    def _create_file(self):
        if self._check(self.secret_file):
            return False
        secrets = {
            'NAME': '',
            'USER': '',
            'PASSWORD': '',
            'SECRET_KEY': 'NOT A SECRET',
        }
        with open(self.secret_file, 'w') as file:
            json.dump(secrets, file)
        return True

    def handle(self):
        if self._create_settings():
            msg_set = "The settings was created successly."
        else:
            msg_set = "You have already created the settings."
        if self._create_file():
             msg_file = "The secrets.json was created successly."
        else:
            msg_file = "The secrets.json already exists."
        msg = (
            "***************************************************************\n"
            f"{msg_set}\n"
            "***************************************************************\n"
            f"{msg_file}\n"
        )
        print(msg)
