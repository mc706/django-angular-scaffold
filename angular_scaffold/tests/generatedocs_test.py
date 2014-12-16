import unittest
import shutil
import os

from angular_scaffold.management.commands.helpers._generate_docs import generate_docs


class GenerateDocsTest(unittest.TestCase):
    def setUp(self):
        self.BASE_DIR = ''

    def test_scaffold(self):
        generate_docs(self.BASE_DIR)
        self.assertTrue(os.path.exists(os.path.join(self.BASE_DIR, 'docs')))
        self.assertTrue(os.path.exists(os.path.join(self.BASE_DIR, 'docs', 'styling.md')))
        self.assertTrue(os.path.exists(os.path.join(self.BASE_DIR, 'docs', 'scaffold.md')))

    def tearDown(self):
        shutil.rmtree(os.path.join(self.BASE_DIR, 'docs'))