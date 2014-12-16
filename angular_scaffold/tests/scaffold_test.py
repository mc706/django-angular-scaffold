import unittest
import shutil
import os

from angular_scaffold.management.commands.helpers._generate_assets import generate_assets


class ScaffoldTest(unittest.TestCase):

    def setUp(self):
        self.BASE_DIR = ''

    def test_scaffold(self):
        generate_assets(self.BASE_DIR)
        self.assertTrue(os.path.exists(os.path.join(self.BASE_DIR,'assets')))

    def tearDown(self):
        shutil.rmtree(os.path.join(self.BASE_DIR), 'assets')

