import unittest
import shutil
import os

from angular_scaffold.management.commands.helpers._generate_assets import generate_assets
from angular_scaffold.management.commands.helpers._generate_csrf import generate_csrf


class GenerateCsrfTest(unittest.TestCase):
    def setUp(self):
        self.BASE_DIR = os.path.dirname(__file__)
        if os.path.exists(os.path.join(self.BASE_DIR, 'assets')):
            shutil.rmtree(os.path.join(self.BASE_DIR, 'assets'))
        generate_assets(self.BASE_DIR, 'test-app')

    def test_debugger(self):
        generate_csrf(self.BASE_DIR)
        self.assertTrue(os.path.exists(os.path.join(self.BASE_DIR, 'assets', 'app', 'config', 'csrf.js')))

    def tearDown(self):
        shutil.rmtree(os.path.join(self.BASE_DIR, 'assets'))

