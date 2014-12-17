import unittest
import shutil
import os

from angular_scaffold.management.commands.helpers._generate_assets import generate_assets
from angular_scaffold.management.commands.helpers._generate_service import generate_service


class StartServiceTest(unittest.TestCase):
    def setUp(self):
        self.BASE_DIR = os.path.dirname(__file__)
        if os.path.exists(os.path.join(self.BASE_DIR, 'assets')):
            shutil.rmtree(os.path.join(self.BASE_DIR, 'assets'))
        generate_assets(self.BASE_DIR, 'test-app')

    def test_view(self):
        generate_service(self.BASE_DIR, 'test', '/', 'tests')
        self.assertTrue(
            os.path.exists(os.path.join(self.BASE_DIR, 'assets', 'app', 'services', 'testService.js')))
        with open(os.path.join(self.BASE_DIR, 'assets', 'app', 'services', 'testService.js'), 'r') as js:
            service = js.read()
            self.assertTrue('listTests' in service)
            self.assertTrue('getTest' in service)
            self.assertTrue('createTest' in service)
            self.assertTrue('updateTest' in service)
            self.assertTrue('deleteTest' in service)

    def tearDown(self):
        shutil.rmtree(os.path.join(self.BASE_DIR, 'assets'))