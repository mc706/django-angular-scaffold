import unittest
import shutil
import os

from angular_scaffold.management.commands.helpers._generate_assets import generate_assets
from angular_scaffold.management.commands.helpers._generate_routes import generate_routes


class StartRouteTest(unittest.TestCase):
    def setUp(self):
        self.BASE_DIR = os.path.dirname(__file__)
        if os.path.exists(os.path.join(self.BASE_DIR, 'assets')):
            shutil.rmtree(os.path.join(self.BASE_DIR, 'assets'))
        generate_assets(self.BASE_DIR, 'test-app')

    def test_view(self):
        generate_routes(self.BASE_DIR)
        self.assertTrue(
            os.path.exists(os.path.join(self.BASE_DIR, 'assets', 'app', 'config', 'routes.js')))
        with open(os.path.join(self.BASE_DIR, 'assets', 'app', 'config', 'routes.js'), 'r') as js:
            routes = js.read()
            self.assertTrue('app.config(["$routeProvider", function ($routeProvider) {' in routes)

    def tearDown(self):
        shutil.rmtree(os.path.join(self.BASE_DIR, 'assets'))