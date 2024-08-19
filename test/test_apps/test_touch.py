import unittest
import os
import tempfile
from apps.touch import Touch
from error import ArgumentError, FileError


class TestTouch(unittest.TestCase):
    @classmethod
    def setup(self, files=None):
        self.test_dir = tempfile.TemporaryDirectory()
        self.temp_path = self.test_dir.name

        if files:
            for file in files:
                # Create the file
                with open(os.path.join(self.temp_path, file), "w") as f:
                    f.write("")

        os.chdir(self.temp_path)
        return []

    @classmethod
    def teardown(self):
        self.test_dir.cleanup()

    def test_touch_single_file(self):
        out = self.setup()
        Touch().execute(["file1.txt"], out)
        self.assertTrue(os.path.isfile("file1.txt"))
        self.teardown()

    def test_touch_existing_file(self):
        out = self.setup(["existing_file.txt"])
        with self.assertRaises(FileError):
            Touch().execute(["existing_file.txt"], out)
        self.teardown()

    def test_touch_wrong_number_of_arguments(self):
        out = self.setup()
        with self.assertRaises(ArgumentError):
            Touch().execute(["file1.txt", "file2.txt"], out)
        self.teardown()
