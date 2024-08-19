import unittest
from application_factory import ApplicationFactory


class TestApplicationFactory(unittest.TestCase):
    def test_safe_apps(self):
        expected_output = 24
        self.assertEqual(
            expected_output,
            len(ApplicationFactory(unsafe=False).application_map),
        )

    def test_unsafe_apps(self):
        expected_output = 48
        self.assertEqual(
            expected_output,
            len(ApplicationFactory().application_map),
        )
