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
BASE_DIR_SETTINGS = os.path.join(project, project_name)


SETTINGS_PATH = os.path.join(BASE_DIR_SETTINGS, 'settings')
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

settings_files = os.listdir('tpl')

for file in settings_files:
    shutil.copy(file, SETTINGS_PATH)

create_file(SETTINGS_PATH)

msg = (
    "Basic settings are created! \n"
    "ATTENTION! You have created the basic settings "
    "for launching in production, use 'python manage.py secrets'!\n"
    "If you want to add more secret variables, "
    " use 'python manage.py secrets --add'."
    "To use 'python manage.py secrets add' - please add in settings "
    "INSTALLED_APPS = ('django_secresy',)\n"
    "Happy coding! :)\n"
)
print(msg)