import re
from setuptools import setup

# Read version from file
VERSION_FILE = 'angular_scaffold/_version.py'
version_text = open(VERSION_FILE, "rt").read()
VSRE = r"^__version__ = ['\"]([^'\"]*)['\"]"
mo = re.search(VSRE, version_text, re.M)
if mo:
    version = mo.group(1)
else:
    raise RuntimeError("Unable to find version string in %s." % (VERSION_FILE,))

# Setup
setup(
    name='django-angular-scaffold',
    version=version,
    url='https://github.com/mc706/django-angular-scaffold',
    author='Ryan McDevitt',
    author_email='mcdevitt.ryan@gmail.com',
    license='Apache License 2.0',
    packages=['angular_scaffold', 'angular_scaffold.management'],
    include_package_data=True,
    description='AngularJS Scaffolding for Django',
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Operating System :: OS Independent",
        "Topic :: Software Development :: Libraries",
        "Topic :: Utilities",
        "Environment :: Web Environment",
        "Framework :: Django",
    ],
)