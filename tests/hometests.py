import unittest
from app import app


class TempTests(unittest.TestCase):

    def test_app_exists(self):
        self.assertTrue(app is not None)
