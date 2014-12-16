from setuptools import setup

import re
VERSIONFILE="angular_scaffold/_version.py"
verstrline = open(VERSIONFILE, "rt").read()
VSRE = r"^__version__ = ['\"]([^'\"]*)['\"]"
mo = re.search(VSRE, verstrline, re.M)
if mo:
    verstr = mo.group(1)
    major, minor, patch = verstr.split('.')
    release = "%s.%s" %(major, minor)
else:
    raise RuntimeError("Unable to find version string in %s." % (VERSIONFILE,))
# Setup
setup(
    name='django-angular-scaffold',
    version=verstr,
    url='https://github.com/mc706/django-angular-scaffold',
    author='Ryan McDevitt',
    author_email='mcdevitt.ryan@gmail.com',
    license='MIT License',
    packages=['angular_scaffold', 'angular_scaffold.management', 'angular_scaffold.management.commands', 'angular_scaffold.management.commands.helpers'],
    include_package_data=True,
    description='AngularJS Scaffolding for Django',
    download_url = 'https://github.com/mc706/django-angular-scaffold/tarball/' + release,
    keywords = ['django', 'angular', 'scaffold'],
    classifiers = [],
)