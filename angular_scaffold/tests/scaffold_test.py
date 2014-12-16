import unittest
import shutil
import os

from angular_scaffold.management.commands.helpers._generate_assets import generate_assets


class ScaffoldTest(unittest.TestCase):

    def setUp(self):
        self.BASE_DIR = os.path.dirname(__file__)
        if os.path.exists(os.path.join(self.BASE_DIR, 'assets')):
            shutil.rmtree(os.path.join(self.BASE_DIR, 'assets'))

    def test_scaffold(self):
        generate_assets(self.BASE_DIR, 'test-app')
        self.assertTrue(os.path.exists(os.path.join(self.BASE_DIR,'assets')))
        self.assertTrue(os.path.exists(os.path.join(self.BASE_DIR,'assets','app')))
        self.assertTrue(os.path.exists(os.path.join(self.BASE_DIR,'assets','lib')))

    def tearDown(self):
        shutil.rmtree(os.path.join(self.BASE_DIR, 'assets'))

