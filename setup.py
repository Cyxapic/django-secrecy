from setuptools import setup, find_packages


setup(
    name="django-secrecy",
    version='0.5',
    include_package_data=True,
    description="Django secret project variables",
    long_description="Django app which generates JSON file with 'secret project variables'",
    author="Artem Sukharenko",
    author_email="truecyxapic@yandex.ru",
    url="https://github.com/Cyxapic/django-secrecy",
    license='MIT',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.6',
    ],
    keywords=['SECRET_KEY', 'Project settings'],
    package_dir={'': 'src'},
    packages=find_packages('src'),
)