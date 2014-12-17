import os
import re


def update_dependencies(directory, dependency):
    with open(os.path.join(directory, 'assets', 'app', 'app.js'), 'r') as f:
        data = f.read()
        search = re.search("angular\.module\(.*(\[.*\])\)", data).groups(0)[0]
        dependencies = eval(search)
        if dependency not in dependencies:
            dependencies.append(dependency)
        replace = str(dependencies)
        updated = data.replace(search, replace)
    with open(os.path.join(directory, 'assets', 'app', 'app.js'), 'w') as f:
        f.write(updated)