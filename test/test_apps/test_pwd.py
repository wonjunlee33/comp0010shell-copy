import tempfile
import unittest
import os
from pathlib import Path
from apps.pwd import Pwd


class TestPwd(unittest.TestCase):
    @classmethod
    def setup(self):
        self.test_dir = tempfile.TemporaryDirectory()
        self.temp_path = Path(self.test_dir.name)
        os.chdir(self.temp_path)
        return []

    @classmethod
    def teardown(self):
        self.test_dir.cleanup()

    def test_pwd(self):
        out = self.setup()
        expected_output = str(self.temp_path) + "\n"
        Pwd().execute([], out)
        self.assertEqual(expected_output, "".join(out))
        self.teardown()

    def test_pwd_root(self):
        out = self.setup()
        os.chdir("/")
        expected_output = "/\n"
        Pwd().execute([], out)
        self.assertEqual(expected_output, "".join(out))
        self.teardown()
