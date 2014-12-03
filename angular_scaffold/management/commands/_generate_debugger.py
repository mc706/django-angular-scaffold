import os
import hashlib

def generate_debugger(directory, password):
    m = hashlib.md5()
    m.update(password)
    hash = m.hexdigest()
    file = os.path.join(directory, 'assets', 'app', 'config', 'logger.js')
    print "Creating: " + file
    with open(file, 'w') as f:
        f.write("""app.config(function ($logProvider) {
    "use strict";
    //Enables debug when ?debug=1&password=*password*
    var password = "%s",
        querystring = (window.location.search ? window.location.search.substring(1) :
                window.location.hash.indexOf('?') !== -1 ? window.location.hash.split('?')[1] : ""),
        params = {};
    angular.forEach(querystring.split('&'), function (pair) {
        params[pair.split('=')[0]] = pair.split('=')[1];
    });
    $logProvider.debugEnabled(false);
    if (params.hasOwnProperty('debug') && params.hasOwnProperty('password')) {
        if (params.debug && md5(params.password) === password) {
            $logProvider.debugEnabled(true);
            console.info("Logging Enabled");
            console.log = function () {};
        }
    }
});
""" % hash)
    _debugger_docs = """#Logging

The logs of this project are using angular's `$logProvider` service. By default
they are disabled, however, you can enable them in the browser by passing the proper credentials.

##Enabling Logging

To enable logging in the browser, pass the following query string on the end of your URL:

```
?debug=1&password=%s
```

##Using Logging

Now that logging can be enabled and disabled for debugging, make sure you provide good,
logging via `$log.debug(message)`. This functionally replaces `console.log()`.
""" % password
    if not os.path.exists(os.path.join(directory, 'docs')):
        os.makedirs(os.path.join(directory, 'docs'))
    with open(os.path.join(directory, 'docs', 'logging.md'), 'w') as f:
        f.write(_debugger_docs)







