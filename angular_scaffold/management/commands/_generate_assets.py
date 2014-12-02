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
            _touch(pwd + '/' + assets[child])
        else:
            if not os.path.exists(child):
                os.makedirs(pwd + '/' + child)
            _build(assets[child], pwd + '/' + child)


def generate_assets(dir):
    if not os.path.exists(dir+'/assets'):
        os.makedirs(dir+'/assets')
    _build(_assets, dir+'/assets')
    app_name = raw_input("Angular Application Name: ")
    with open(dir + '/assets/app/app.js','w') as app:
        app.write('var app = angular.module("%s", []);' % app_name)

if __name__ == "__main__":
    generate_assets('../..')



