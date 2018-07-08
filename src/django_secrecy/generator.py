import os
import sys
import shutil
import argparse
import json

from .utils import create_file


parser = argparse.ArgumentParser()
parser.add_argument("project_name", help="Django project name")
args = parser.parse_args()
project_name = args.project_name

BASE_DIR = os.path.join(sys.path[-1].split('lib')[0], project_name)
BASE_DIR_SETTINGS = os.path.join(BASE_DIR, project_name)
SETTINGS_PATH = os.path.join(BASE_DIR_SETTINGS, 'settings')

def main():
    try:
        os.mkdir(SETTINGS_PATH)
    except FileExistsError:
        msg = (
            "You have already created the settings.\n"
            "To add secret values, use 'python manage.py secrets --add' "
            "from your project."
        )
        print(msg)
        exit()

    TPL = os.path.dirname(os.path.abspath(__file__))
    TPL = os.path.join(TPL, 'tpl')
    settings_files = [os.path.join(TPL, file) for file in os.listdir(TPL)
                                              if file != '__pycache__']
    for file in settings_files:
        try:
            shutil.copy(file, SETTINGS_PATH)
        except FileNotFoundError:
            print(f'Error >{file}')

    create_file(SETTINGS_PATH)

    msg = (
        "Basic settings are created! \n"
        "ATTENTION! You have created the basic settings "
        "for launching in production, use 'python manage.py secrets'!\n"
        "If you want to add more secret variables, "
        " use 'python manage.py secrets --add'."
        "To use 'python manage.py secrets add' - please add in settings "
        "INSTALLED_APPS = ('django_secresy',)\n"
        "Do not forget to add 'development.py' to .gitignore\n"
        "Happy coding! :)\n"
    )
    print(msg)
    # delete default settings file
    os.remove(os.path.join(BASE_DIR_SETTINGS, 'settings.py'))


if __name__ == '__main__':
    main()