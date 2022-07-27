import os
from setuptools import find_packages, setup

with open(os.path.join(os.path.dirname(__file__), 'README.md')) as readme:
    README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='django-admin-autoregister',
    version='1.1.0',
    packages=find_packages(),
    include_package_data=True,
    license='MIT License',
    description='A Django app that registers all unregistered models to the admin automatically.',
    long_description=README,
    long_description_content_type="text/markdown",
    url='https://github.com/janezkranjc/django-admin-autoregister',
    author='Janez Kranjc',
    author_email='janez.kranjc@gmail.com',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Framework :: Django :: 2.2',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
)
