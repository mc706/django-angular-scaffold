import os
from string import Template

_template = Template("""app.controller("${name}Controller", function ($$scope, $$location, $$log) {
    'use strict';
    $$log.debug("${name} Controller Initialized");
});""")

def generate_controller(directory, name):
    controller = os.path.join("app", "controllers", name.lower() + "Controller.js")
    title = name.title()
    with open(os.path.join(directory, 'assets', controller), 'w') as f:
        f.write(_template.substitute(name=title))

if __name__ == "__main__":
    generate_controller('../..', 'category')