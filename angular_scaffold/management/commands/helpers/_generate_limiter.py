import os


_limiter = """app.run(["$rootScope", "$log", function ($rootScope, $log) {
    "use strict";
    $rootScope.limiter = {};
    $rootScope.limit = 1000; // 1 second

    $rootScope.checkLimiter = function (d, key, limit) {
        var timeSinceLastGet = $rootScope.limiter[key] ? new Date().getTime() - $rootScope.limiter[key] : null,
            rlimit = limit || $rootScope.limit;
        if ($rootScope.limiter[key] && timeSinceLastGet < rlimit) {
            $log.debug('call rejected', $rootScope.limiter);
            d.reject();
        }
        $rootScope.limiter[key] = new Date().getTime();
    };
}]);"""

_docs = """#Rate Limiter

Included in your `app/config` folder is `limiter.js`. This runtime config file gives access to a call rate limiter
funciton.

##Use

In a service, you can call `$rootScope.checkLimiter(defer, key, optional_time)`.

* `defer` - Pass in the defer object. It will call defer.reject() if the call is made too close the previous one.
* `key` - Pass in the key for the array of calls. Usually I pass in the service call name.
* `optiona_time` - overrides the default value which is 1 second.
"""


def generate_limiter(directory):
    filename = os.path.join(directory, 'assets', 'app', 'config', 'limiter.js')
    print "Creating: " + filename
    with open(filename, 'w') as f:
        f.write(_limiter)
    if not os.path.exists(os.path.join(directory, 'docs')):
        os.makedirs(os.path.join(directory, 'docs'))
    with open(os.path.join(directory, 'docs', 'limiter.md'), 'w') as f:
        f.write(_docs)
