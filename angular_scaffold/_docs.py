docs = """django-angular-scaffold
=======================

[![Build Status](https://travis-ci.org/mc706/django-angular-scaffold.svg?branch=master)](https://travis-ci.org/mc706/django-angular-scaffold)
[![PyPI version](https://badge.fury.io/py/django-angular-scaffold.svg)](http://badge.fury.io/py/django-angular-scaffold)
[![Code Health](https://landscape.io/github/mc706/django-angular-scaffold/master/landscape.svg)](https://landscape.io/github/mc706/django-angular-scaffold/master)
[![Coverage Status](https://img.shields.io/coveralls/mc706/django-angular-scaffold.svg)](https://coveralls.io/r/mc706/django-angular-scaffold)

set of django management commands to scaffold a django + angular project

##Installation

Install using pip

```
pip install django-angular-scaffold
```

include in your INSTALLED_APPS
```
#settings.py
...
INSTALLED_APPS = (
    ...
    'angular_scaffold',
    ...
)
```

##Commands

The following are commands that are made available through this package.


###scaffold

```
./manage.py scaffold
```

Builds a assets folder structure in the following structure:

```
/assets
    + - app
    |   + - config
    |   + - controllers
    |   + - directives
    |   + - services
    |   + - views
    |   + - app.js
    + - lib
        + - fonts
        + - scripts
        + - styles
            + - site
            |   + - _global.scss
            |   + - _mixins.scss
            |   + - _variables.scss
            + - vendor
            + styles.scss
```

It will prompt for an application name, this will add start the angular app off.

It also automatically setups the `styles.scss` to import the pre stubbed out globals, mixins, and variables files.

The rest of the folders are stubbed out with a `.gitkeep` file to allow the directory structure to be added to git.


###startview

```
./manage.py startview <viewname>
```

creates new view, creates new styles and adds it to the import

Can accept a path. The following are valid viewname arguments

```
./manage startview homepage
./manage startview home-page
./manage startview ticket/new
./manage startview settings/options/test
```
This will create a view file in the appropriate folder, create a mirrored scss file in the site directory, and
import the style into the main styles.scss file.

###generatedocs

```
./manage.py generatedocs
```

Adds a `/docs` folder and copies some basic documentation into it

###createdebugger

```
./manage.py createdebugger <password>
```

Creates a config file for angular that overrides console.log and replaces it with
$log.debug. Then disables $log.debug unless a query string with an encoded password
is included. 

This makes it very easy to debug your application without having to expose the underlying 
to the users. It also allows you to keep your logging statements in your app when going to 
production, as they are turned off and hidden by default. 

###startservice

```
./manage.py startservice <service_name>
```

Creates a starter service. Will ask for the endpoint, and the pluralization of the service name,
and will create list, get, post, put, and delete methods for that service. 

###startcontroller

```
./manage.py startcontroller <controller_name>
```

Creates a new empty controller in controllers directory.

###createcsrf

```
./manage.py createcsrf
```

Adds the csrf token to your angular ajax headers in a config file. Also injects the `ngCookies` dependency into your app.

###startroutes

```
./manage.py startroutes
```

Adds a routes config file and inject ngRoute as a dependency. 
Creates a defaulted route to `/` using `HomeController` and `views/home.html`.

###addroute

```
./manage.py addroute
```

Adds a route to the routes. Will prompt for url, controller, views, and a number of variables to resolve. 

###createlimiter

```
./manage.py createlimiter
```

Adds a runtime config that gives access to a `$rootScope.checkLimiter()` function that you can use in services
to limit the number of calls made. """