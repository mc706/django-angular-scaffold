from fabric.api import local, settings


def bump_patch():
    with open('angular_scaffold/_version.py', 'r') as f:
        original = f.read()
        version = original.split('=')[1].strip('\" \n\'')
        major, minor, patch = version.split('.')
        patch = int(patch) + 1
    with open('angular_scaffold/_version.py', 'w') as f:
        f.write('__version__ = "%s.%s.%s"' % (major, minor, patch))
    local('git add angular_scaffold/_version.py')
    local('git commit -m "updated version to %s.%s.%s"' % (major, minor, patch))
    local('git push')


def bump_minor():
    with open('angular_scaffold/_version.py', 'r') as f:
        original = f.read()
        version = original.split('=')[1].strip('\" \n\'')
        major, minor, patch = version.split('.')
        patch = 0
        minor = int(minor) + 1
    with open('angular_scaffold/_version.py', 'w') as f:
        f.write('__version__ = "%s.%s.%s"' % (major, minor, patch))
    local('git add angular_scaffold/_version.py')
    local('git commit -m "updated version to %s.%s.%s"' % (major, minor, patch))
    local('git tag %s.%s -m "Update for release"' % (major, minor))
    local('git push --tags origin master')


def bump_major():
    with open('angular_scaffold/_version.py', 'r') as f:
        original = f.read()
        version = original.split('=')[1].strip('\" \n\'')
        major, minor, patch = version.split('.')
        patch = 0
        minor = 0
        major = int(major) + 1
    with open('angular_scaffold/_version.py', 'w') as f:
        f.write('__version__ = "%s.%s.%s"' % (major, minor, patch))
    local('git add angular_scaffold/_version.py')
    local('git commit -m "updated version to %s.%s.%s"' % (major, minor, patch))
    local('git tag %s.%s -m "Update for release"' % (major, minor))
    local('git push --tags origin master')


def update_generated_docs():
    with settings(warn_only=True):
        with open("README.md", 'r') as readme, open('angular_scaffold/_docs.py', 'w') as docs:
            documentation = readme.read()
            docs.write('docs = """')
            docs.write(documentation)
            docs.write('"""')
        local('git add angular_scaffold/_docs.py')
        local('git commit -m "updated generated docs"')


def deploy_test(release='patch'):
    update_generated_docs()
    if release == 'patch':
        bump_patch()
    elif release == 'minor':
        bump_minor()
    elif release == 'major':
        bump_major()
    elif release == 'none':
        pass
    else:
        bump_patch()
    local('python setup.py register -r pypitest')
    local('python setup.py sdist upload -r pypitest')


def deploy(release='patch'):
    update_generated_docs()
    if release == 'patch':
        bump_patch()
    elif release == 'minor':
        bump_minor()
    elif release == 'major':
        bump_major()
    elif release == 'none':
        pass
    else:
        bump_patch()
    local('python setup.py register -r pypi')
    local('python setup.py sdist upload -r pypi')


def deploy_both(release='patch'):
    deploy_test(release)
    deploy('none')