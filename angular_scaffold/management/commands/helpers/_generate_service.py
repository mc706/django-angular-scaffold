import os
from string import Template

_template = Template("""        ${name}${title}: function (${args}) {
            var defer = $$q.defer();
            $$http({
                method: "${method}",
                url: "${url}"${ext}${dataline}
            }).success(function (data, status, headers, config) {
                defer.resolve(data);
            }).error(function (data, status, headers, config) {
                defer.reject(status);
            });
            return defer.promise;
        }""")
_endpoints = [
    {
        'name': 'list',
        'method': 'GET',
        'args': None,
        'ext': None,
        'data': None,
        'plural': True
    },
    {
        'name': 'get',
        'method': 'GET',
        'args': 'id',
        'ext': ' + id + "/"',
        'data': None,
        'plural': False
    },
    {
        'name': 'create',
        'method': 'POST',
        'args': 'data',
        'ext': None,
        'data': 'data',
        'plural': False
    },
    {
        'name': 'update',
        'method': 'PUT',
        'args': 'id, data',
        'ext': ' + id + "/"',
        'data': 'data',
        'plural': False
    },
    {
        'name': 'delete',
        'method': 'DELETE',
        'args': 'id',
        'ext': ' + id + "/"',
        'data': None,
        'plural': False
    },

]


def generate_service(directory, name=None, url=None, plural=None):
    if not name:
        name = raw_input("Service Name: ")
    if not url:
        url = raw_input("Endpoint URL: ")
    if not plural:
        plural = raw_input("Plural Form: ")
    endpoints = []
    service = os.path.join("app", "services", name.lower() + "Service.js")
    with open(os.path.join(directory, 'assets', service), 'w') as f:
        f.write("""app.service('%sService', ["$http", "$q", function ($http, $q) {
    'use strict';
    return {
""" % name.title())
        for method in _endpoints:
            title = name.title()
            if method['data']:
                dataline = ",\n                data: data"
            else:
                dataline = ''
            if method['ext']:
                extensions = method['ext']
            else:
                extensions = ""
            if method['args']:
                arguments = method['args']
            else:
                arguments = ""
            if method['plural']:
                title = plural.title()
            serv = _template.substitute(
                name=method['name'],
                title=title,
                args=arguments,
                method=method['method'],
                url=url,
                ext=extensions,
                dataline=dataline
            )
            endpoints.append(serv)
        f.write(',\n'.join(endpoints))
        f.write("""\n
    };
}]);""")