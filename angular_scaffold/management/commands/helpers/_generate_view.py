import os


def _touch(fname):
    try:
        os.utime(fname, None)
    except Exception:
        open(fname, 'a').close()
    return fname


def _build(path, pwd=None):
    current = path.pop(0)
    if pwd:
        here = os.path.join(pwd, current)
    else:
        here = current
    if not path:
        return _touch(here)
    else:
        if not os.path.exists(here):
            os.makedirs(here)
        _build(path, here)


def generate_view(directory, name=None):
    if not name:
        name = raw_input('View Name: ')
    view = os.path.join("assets", "app", "views", name + ".html")
    split = name.split(os.sep)
    namespace = '-'.join(split)
    filename = split[-1]
    split[-1] = "_" + filename + ".scss"
    style = os.path.join("assets", "lib", "styles", "site", os.sep.join(split))

    # view html file
    if not os.path.exists(os.path.join(directory, view)):
        _build(view.split(os.sep), directory)
        with open(os.path.join(directory, view), 'w') as f:
            f.write("<div class='page %s'>\n\n</div>" % namespace)
    else:
        print "View Template Already Exists: %s" % namespace

    # styles file
    if not os.path.exists(os.path.join(directory, style)):
        _build(style.split(os.sep), directory)
        with open(os.path.join(directory, style), 'w') as f:
            f.write(".page.%s{\n\n}" % namespace)
    else:
        print "View Styles Already Exists: %s" % style

    # import styles styles
    with open(os.path.join(directory, 'assets', 'lib', 'styles', 'styles.scss'), 'a') as styles:
        styles.write('\n@import "site/%s";' % name)