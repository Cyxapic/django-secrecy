from .generator import Generator


def main():
    generator = Generator()
    generator.handle()
    msg = (
        "***************************************************************\n"
        "Basic settings are created! \n"
        "ATTENTION! You have created the basic settings "
        "for launching in production, use 'python manage.py secrets'!\n"
        "To add secret values, use 'python manage.py secrets --add' \n"
        "To use 'python manage.py secrets add' - please add in settings "
        "INSTALLED_APPS = ('django_secresy',)\n"
        "Do not forget to add 'development.py' to .gitignore\n"
        "Happy coding! :)\n"
        "***************************************************************\n"
    )
    print(msg)


if __name__ == '__main__':
    main()