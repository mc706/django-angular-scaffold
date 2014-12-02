import os
from string import Template

_template = Template("""app.controller("${name}Controller", function ($$scope, $$location, $$log) {
    'use strict';
    $$log.debug("${name} Controller Initialized");
});""")

def generate_controller(dir, name):
    controller = "app" + os.sep + "controllers" + os.sep + name.lower() + "Controller.js"
    title = name.title()
    with open(dir + os.sep + 'assets' + os.sep + controller, 'w') as f:
        f.write(_template.substitute(name=name.title()))

if __name__ == "__main__":
    generate_controller('../..', 'category')