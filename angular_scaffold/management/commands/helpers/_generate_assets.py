import os


_assets = {
    "app": {
        "config": {
            ".gitkeep": ".gitkeep"
        },
        "controllers": {
            ".gitkeep": ".gitkeep"
        },
        "directives": {
            ".gitkeep": ".gitkeep"
        },
        "services": {
            ".gitkeep": '.gitkeep'
        },
        "views": {
            ".gitkeep": ".gitkeep"
        },
        "app.js": "app.js"
    },
    "lib": {
        "fonts": {
            ".gitkeep": ".gitkeep"
        },
        "scripts": {
            ".gitkeep": ".gitkeep"
        },
        "styles": {
            "site": {
                "_global.scss": "_global.scss",
                "_mixins.scss": "_mixins.scss",
                "_variables.scss": "_variables.scss",
            },
            "vendor": {
                ".gitkeep": ".gitkeep"
            },
            "styles.scss": "styles.scss"
        }
    }
}


def _touch(fname):
    try:
        os.utime(fname, None)
    except:
        open(fname, 'a').close()


def _build(assets, pwd):
    for child in assets:
        if (type(assets[child]) is str):
            _touch(pwd + os.sep + assets[child])
        else:
            if not os.path.exists(child):
                os.makedirs(pwd + os.sep + child)
            _build(assets[child], pwd + os.sep + child)


def generate_assets(dir):
    if not os.path.exists(os.path.join(dir, 'assets')):
        os.makedirs(os.path.join(dir, 'assets'))
    _build(_assets, os.path.join(dir, 'assets'))
    # setup angular application
    app_name = raw_input("Angular Application Name: ")
    with open(os.path.join(dir, 'assets', 'app', 'app.js'), 'w') as app:
        app.write('var app = angular.module("%s", []);' % app_name)
    # setup styles
    with open(os.path.join(dir, 'assets', 'lib', 'styles', 'styles.scss'), 'w') as styles:
        styles.write('//setup\n'
                     '@import "site/variables";\n'
                     '@import "site/mixins";\n'
                     '\n'
                     '//vendor\n'
                     '\n'
                     '//site\n'
                     '@import "site/global";\n')


if __name__ == "__main__":
    generate_assets('../..')



