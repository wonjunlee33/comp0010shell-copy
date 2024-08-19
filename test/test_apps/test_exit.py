import unittest
from apps.exit import Exit


class TestExit(unittest.TestCase):
    def test_exit(self):
        with self.assertRaises(SystemExit):
            Exit().execute()
