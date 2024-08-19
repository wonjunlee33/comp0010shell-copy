import unittest
from apps.color import Color
from error import ArgumentError, FlagError


class TestColor(unittest.TestCase):
    @classmethod
    def setup(self):
        return []

    @classmethod
    def teardown(self):
        print("\033[0m")
        pass

    def test_color(self):
        out = self.setup()
        expected_output = "\033[31m"
        Color().execute(["red"], out)
        self.assertEqual("".join(out), expected_output)
        self.teardown()

    def test_color_two_words(self):
        out = self.setup()
        expected_output = "\033[91m"
        Color().execute(["light red"], out)
        self.assertEqual("".join(out), expected_output)
        self.teardown()

    def test_color_invalid(self):
        out = self.setup()
        with self.assertRaises(FlagError):
            Color().execute(["darkgrey"], out)
        self.teardown()

    def test_color_no_args(self):
        out = self.setup()
        with self.assertRaises(ArgumentError):
            Color().execute([], out)

    def test_color_too_many_args(self):
        out = self.setup()
        with self.assertRaises(ArgumentError):
            Color().execute(["red", "blue", "green"], out)
        self.teardown()
