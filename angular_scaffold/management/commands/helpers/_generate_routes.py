import os

from angular_scaffold.management.commands.helpers._update_dependencies import update_dependencies


_routes = """app.config(["$routeProvider", function ($routeProvider) {
    "use strict";
    $routeProvider.when('/',
        {
            controller: 'HomeController',
            templateUrl: '../app/views/home.html',
            resolve: {}
        })
        .otherwise({redirectTo: '/'});
}]);"""


def generate_routes(directory):
    filename = os.path.join(directory, 'assets', 'app', 'config', 'routes.js')
    print "Creating: " + filename
    with open(filename, 'w') as f:
        f.write(_routes)
    print "Injecting route dependency"
    update_dependencies(directory, 'ngRoute')