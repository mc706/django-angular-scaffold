import os
from _update_dependencies import update_dependencies

_csrf = """app.run(function ($http, $cookies) {
    "use strict";
    $http.defaults.headers.common['X-CSRFToken'] = $cookies.csrftoken;
});"""


def generate_csrf(directory):
    filename = os.path.join(directory, 'assets', 'app', 'config', 'csrf.js')
    print "Creating: " + filename
    with open(filename, 'w') as f:
        f.write(_csrf)
    print "Injecting cookie dependency"
    update_dependencies(directory, 'ngCookies')

if __name__ == '__main__':
    generate_csrf('../..')










