import os

styling_docs = """#Style Guide

This project uses SASS. All styles are stored in `/assets/lib/styles/`.

## Single Style File

Name all scss files except for `styles.scss` prepended with a `_`.

Scss compilers do not compile files that start with a `_`.

You can import your files in `styles.scss` by name, excluding the `_` and the `.scss`

`@import ''vendor/bootstrap'';`


`@import ''site/global'';`

## Vendor Styles

All vendor styles should be put in the `lib/styles/vendor`.
They should be imported in the top section of styles.

## Global Styles

The global styles are put in a few files.

* `_global.scss`  - Styles to be used on all pages
* `_variables.scss` - Used to set sizes and colors globally
* `_mixins.scss` - A collection of mixins

## Site Styles

The sites styles should mirror the angular views in the `/assets/app/views`

For Example:

This app structure

```
assets/app/
    |
    + - config
    + - controllers
    + - directoryectives
    + - services
    + - views
    |       |
    |       + - settings
    |       |       |
    |       |       + - settings.html
    |       |       + - permissions.html
    |       |       + - notifications.html
    |       + - profile
    |       |       |
    |       |       + profile.html
    |       |       + friends.html
    |       + - home.html
    + app.js
```
should translate into this styles structure
```
assets/lib/styles/
    |
    + - vendor
    + - site
    |       |
    |       + - settings
    |       |       |
    |       |       + - _settings.scss
    |       |       + - _permissions.scss
    |       |       + - _notifications.scss
    |       + - profile
    |       |       |
    |       |       + - _profile.scss
    |       |       + - _friends.scss
    |       + - _home.scss
    |       + - _global.scss
    |       + - _variables.scss
    |       + - _mixins.scss
    + styles.scss
```
Which would result in a styles.scss that looks a little bit like this
```
//vendor sytles
...

//global styles
@import "site/variables";
@import "site/mixins";
@import "site/global";

//page imports
@import "site/settings/settings";
@import "site/settings/permissions";
@import "site/settings/notifications";
@import "site/profile/profile";
@import "site/profile/friends";
@import "site/home";
```
Then each page in views should be wrapped in something like this:
```
<div class="page home">
...
</div>
```
and each site _home.scss file should look like this
```
.page.home{
    h1 {
      .small{
        ...
      }
    }
}
```
The DOM structure of the page should match the hierarchical structure of the scss file.

This setup namespaces all of the styles and makes sure we don't need any inline styles anywhere. It also makes it very easy to write styles for the whole app and handle all the exceptions very easily.
"""

scaffolding_docs = """
django-angular-scaffold
=======================

[![PyPI version](https://badge.fury.io/py/django-angular-scaffold.svg)](http://badge.fury.io/py/django-angular-scaffold)

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
"""
def generate_docs(directory):
    if not os.path.exists(os.path.join(directory, 'docs')):
        os.makedirs(os.path.join(directory, 'docs'))
    with (open(os.path.join(directory, 'docs', 'styling.md'), 'w')) as f:
        f.write(styling_docs)
    with (open(os.path.join(directory, 'docs', 'scaffold.md'), 'w')) as f:
        f.write(scaffolding_docs)



