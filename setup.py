import os

# Use setuptools only if the user opts-in by setting the USE_SETUPTOOLS env var
# This ensures consistent behavior but allows for advanced usage with
# virtualenv, buildout, and others.
USE_SETUPTOOLS = False
if 'USE_SETUPTOOLS' in os.environ:
    try:
        from setuptools import setup
        USE_SETUPTOOLS = True
    except:
        USE_SETUPTOOLS = False


if USE_SETUPTOOLS is False:
    from distutils.core import setup

README  = open(os.path.join(os.path.dirname(__file__), 'README.rst')).read()
LICENSE = open(os.path.join(os.path.dirname(__file__), 'LICENSE')).read()

# Tell distutils to put the data_files in platform-specific installation
# locations. See here for an explanation:
# http://groups.google.com/group/comp.lang.python/browse_thread/thread/35ec7b2fed36eaec/2105ee4d9e8042cb
from distutils.command.install import INSTALL_SCHEMES
for scheme in INSTALL_SCHEMES.values():
    scheme['data'] = scheme['purelib']

DATA_FILES = []
DATA_PATH = 'django_saltapi'
for dirpath, dirnames, filenames in os.walk(DATA_PATH, topdown=True):
    # Ignore dirnames that start with '.'
    for i, dirname in enumerate(dirnames):
        if dirname.startswith('.'): del dirnames[i]
    if filenames:
        DATA_FILES.append([dirpath, [os.path.join(dirpath, f) for f in filenames]])

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name = 'django-saltapi',
    version = '0.7.5',
    packages = ['django_saltapi'],
    license = LICENSE,
    description = 'This Django app serves as the REST API for Salt.',
    long_description = README,
    url = 'http://www.example.com/',
    author = 'Henrik Holmboe',
    author_email = 'henrik@holmboe.se',
    install_requires=open('requirements.txt').readlines(),
    scripts = [
        'scripts/django-saltapi',
        'scripts/django-saltapi-ping',
        'scripts/django-saltapi-echo',
        ],
    data_files = DATA_FILES,
    classifiers = [
        #'Development Status :: 1 - Planning',
        #'Development Status :: 2 - Pre-Alpha',
        'Development Status :: 3 - Alpha',
        #'Development Status :: 4 - Beta',
        #'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Environment :: Console',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: System :: Distributed Computing',
    ],
)
