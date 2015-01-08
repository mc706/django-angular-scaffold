import unittest
import shutil
import os

from angular_scaffold.management.commands.helpers._generate_assets import generate_assets
from angular_scaffold.management.commands.helpers._generate_view import generate_view


class StartViewTest(unittest.TestCase):
    def setUp(self):
        self.BASE_DIR = os.path.dirname(__file__)
        if os.path.exists(os.path.join(self.BASE_DIR, 'assets')):
            shutil.rmtree(os.path.join(self.BASE_DIR, 'assets'))
        generate_assets(self.BASE_DIR, 'test-app')

    def test_view(self):
        generate_view(self.BASE_DIR, 'home')
        self.assertTrue(os.path.exists(os.path.join(self.BASE_DIR, 'assets', 'app', 'views', 'home.html')))
        self.assertTrue(os.path.exists(os.path.join(self.BASE_DIR, 'assets', 'lib', 'styles', 'site', '_home.scss')))
        with open(os.path.join(self.BASE_DIR, 'assets', 'lib', 'styles', 'styles.scss'), 'r') as scss:
            styles = scss.read()
            self.assertTrue('@import "site/home"' in styles)

    def test_nested_namespace(self):
        generate_view(self.BASE_DIR, 'project/home')
        self.assertTrue(os.path.exists(os.path.join(self.BASE_DIR, 'assets', 'app', 'views', 'project', 'home.html')))
        self.assertTrue(
            os.path.exists(os.path.join(self.BASE_DIR, 'assets', 'lib', 'styles', 'site', 'project', '_home.scss')))
        with open(os.path.join(self.BASE_DIR, 'assets', 'lib', 'styles', 'styles.scss'), 'r') as scss:
            styles = scss.read()
            self.assertTrue('@import "site/project/home"' in styles)


    def tearDown(self):
        shutil.rmtree(os.path.join(self.BASE_DIR, 'assets'))