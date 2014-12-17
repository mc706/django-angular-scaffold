import unittest
import shutil
import os

from angular_scaffold.management.commands.helpers._generate_assets import generate_assets
from angular_scaffold.management.commands.helpers._generate_controller import generate_controller


class StartControllerTest(unittest.TestCase):
    def setUp(self):
        self.BASE_DIR = os.path.dirname(__file__)
        if os.path.exists(os.path.join(self.BASE_DIR, 'assets')):
            shutil.rmtree(os.path.join(self.BASE_DIR, 'assets'))
        generate_assets(self.BASE_DIR, 'test-app')

    def test_view(self):
        generate_controller(self.BASE_DIR, 'home')
        self.assertTrue(
            os.path.exists(os.path.join(self.BASE_DIR, 'assets', 'app', 'controllers', 'homeController.js')))
        with open(os.path.join(self.BASE_DIR, 'assets', 'app', 'controllers', 'homeController.js'), 'r') as js:
            controller = js.read()
            print controller
            self.assertTrue('app.controller("HomeController",' in controller)


    def tearDown(self):
        shutil.rmtree(os.path.join(self.BASE_DIR, 'assets'))

