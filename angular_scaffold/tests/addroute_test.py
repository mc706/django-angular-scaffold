import unittest
import shutil
import os

from angular_scaffold.management.commands.helpers._generate_assets import generate_assets
from angular_scaffold.management.commands.helpers._generate_routes import generate_routes
from angular_scaffold.management.commands.helpers._add_route import add_route


class AddRouteTest(unittest.TestCase):
    def setUp(self):
        self.BASE_DIR = os.path.dirname(__file__)
        if os.path.exists(os.path.join(self.BASE_DIR, 'assets')):
            shutil.rmtree(os.path.join(self.BASE_DIR, 'assets'))
        generate_assets(self.BASE_DIR, 'test-app')
        generate_routes(self.BASE_DIR)

    def test_view(self):
        add_route(self.BASE_DIR, '/', 'HomeController', 'home.html', [])
        self.assertTrue(
            os.path.exists(os.path.join(self.BASE_DIR, 'assets', 'app', 'config', 'routes.js')))
        with open(os.path.join(self.BASE_DIR, 'assets', 'app', 'config', 'routes.js'), 'r') as js:
            routes = js.read()
            print routes
            self.assertTrue('app.config(function ($routeProvider) {' in routes)
            self.assertTrue("controller: 'HomeController'," in routes)
            self.assertTrue("templateUrl: '/static/app/views/home.html'" in routes)

    def test_multiple_view(self):
        add_route(self.BASE_DIR, '/projects/', 'project', 'project/home', ['project'])
        self.assertTrue(
            os.path.exists(os.path.join(self.BASE_DIR, 'assets', 'app', 'config', 'routes.js')))
        with open(os.path.join(self.BASE_DIR, 'assets', 'app', 'config', 'routes.js'), 'r') as js:
            routes = js.read()
            print routes
            self.assertTrue('app.config(function ($routeProvider) {' in routes)
            self.assertTrue("controller: 'ProjectController'," in routes)
            self.assertTrue("templateUrl: '/static/app/views/project/home.html'" in routes)

    def tearDown(self):
        shutil.rmtree(os.path.join(self.BASE_DIR, 'assets'))