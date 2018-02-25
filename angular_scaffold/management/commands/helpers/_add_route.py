import os
import re
import sys
from string import Template

from ._generate_view import generate_view
from ._generate_controller import generate_controller


_route = Template(""".when('${when}',
        {
            controller: '${controller}',
            templateUrl: '${template}'${resolutions}
        })""")

_resolve = Template("""                ${variable}: function (/*Service*/) {
                    return false; //replace with resolved variable call
                }""")
_header = """app.config(function ($routeProvider) {
    "use strict";
    $routeProvider"""

_footer = """.otherwise({redirectTo: '/'});
});"""


def add_route(directory, when=None, controller=None, template=None, resolves=None):
    if (sys.version_info > (3, 0)):
        if not when:
            when = input("When: ")
        if not controller:
            controller = input("Controller: ")
    else:
        if not when:
            when = raw_input("When: ")
        if not controller:
            controller = raw_input("Controller: ")
    if not os.path.exists(os.path.join(directory, 'assets', 'controllers', controller + "Controller.js")):
        generate_controller(directory, controller)
        controller = controller.title() + "Controller"
    else:
        print("Using Controller: %s" % os.path.join(directory, 'assets', 'controllers', controller + "Controller.js"))
    if not template:
        if (sys.version_info > (3, 0)):
            template = input("Template (relative to views folder): ")
        else:
            template = raw_input("Template (relative to views folder): ")
    template_name = template
    if not template_name.endswith('.html'):
        template_html = template_name + '.html'
    else:
        template_html = template_name
    template = '/static/app/views/' + template_html
    if not os.path.exists(os.path.join(directory, 'assets', 'app', 'views', template_html)):
        generate_view(directory, template_name)
    else:
        print("Using Template: %s" % os.path.join(directory, 'assets', 'app', 'views', template_html))
    if resolves is None:
        resolve_input = True
        resolves = []
        while resolve_input:
            if (sys.version_info > (3, 0)):
                resolve_input = input("Resolve: ")
            else:
                resolve_input = raw_input("Resolve: ")
            if resolve_input:
                resolves.append(resolve_input)
    if resolves:
        resolutions = ",\n            resolve: {\n"
        resolutions += ',\n'.join([_resolve.substitute(variable=variable) for variable in resolves])
        resolutions += "\n            }"
    else:
        resolutions = ""
    new_route = _route.substitute(
        when=when,
        controller=controller,
        template=template,
        resolutions=resolutions
    )
    route_regex = '\.when\(.*?\}\)'
    with open(os.path.join(directory, 'assets', 'app', 'config', 'routes.js'), 'r') as route_file:
        data = route_file.read()
        routes = re.findall(route_regex, data, re.DOTALL)
    routes.append(new_route)
    organized_routes = routes
    # TODO: organize routes by route complexity and group them
    with open(os.path.join(directory, 'assets', 'app', 'config', 'routes.js'), 'w') as route_file:
        route_file.write(_header + ''.join(organized_routes) + _footer)
