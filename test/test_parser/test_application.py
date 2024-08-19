import unittest
import tempfile
from pathlib import Path
from application import Application
from error import ApplicationError
from unittest.mock import patch


class TestApplication(unittest.TestCase):
    @classmethod
    def setup(self, contents):
        self.test_dir = tempfile.TemporaryDirectory()
        self.temp_path = Path(self.test_dir.name)
        self.test_file = []
        for i in range(len(contents)):
            self.test_file.append(str(self.temp_path) + f"/test-{i}.txt")
            with open(self.test_file[i], "w") as f:
                f.write(contents[i])
        return []

    @classmethod
    def teardown(self):
        self.test_dir.cleanup()

    def test_application(self):
        self.setup([])
        with self.assertRaises(ApplicationError):
            Application().execute([], [])
        self.teardown()

    def test_application_stdin(self):
        self.setup(["foo bar\n"])
        with patch("sys.stdin", open(self.test_file[0])):
            out = Application().stdin_check()
        self.assertEqual("foo bar\n", "".join(out))
        self.teardown()
