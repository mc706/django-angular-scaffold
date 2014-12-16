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
def generate_docs(directory):
    if not os.path.exists(os.path.join(directory, 'docs')):
        os.makedirs(os.path.join(directory, 'docs'))
    with (open(os.path.join(directory, 'docs', 'styling.md'), 'w')) as f:
        f.write(styling_docs)
    with open(os.path.join(os.path.dirname(__file__),'..','..','..','README.md'), 'r') as fin:
        scaffolding_docs = fin.read()
    with (open(os.path.join(directory, 'docs', 'scaffold.md'), 'w')) as f:
        f.write(scaffolding_docs)


if __name__ == '__main__':
    generate_docs('../../assets')