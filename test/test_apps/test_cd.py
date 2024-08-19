import unittest
import os
import tempfile
from pathlib import Path
from apps.cd import Cd
from apps.pwd import Pwd
from error import ArgumentError, DirectoryError


class TestCd(unittest.TestCase):
    @classmethod
    def setup(self):
        self.test_dir = tempfile.TemporaryDirectory()
        self.temp_path = Path(self.test_dir.name)
        os.chdir(self.temp_path)
        return []

    @classmethod
    def create_directory(self, directory_name):
        os.mkdir(directory_name)

    def teardown(self):
        self.test_dir.cleanup()

    def test_cd(self):
        out = self.setup()
        new_dir = "new_directory"
        self.create_directory(new_dir)
        Cd().execute([new_dir], out)
        expected_path = str(self.temp_path / new_dir)
        # Use Pwd to check the current working directory
        out2 = []
        Pwd().execute([], out2)
        self.assertEqual(expected_path + "\n", out2[0])
        self.teardown()

    def test_cd_wrong_arguments(self):
        out = self.setup()
        with self.assertRaises(ArgumentError):
            Cd().execute([], out)
        self.teardown()

    def test_cd_up_directory(self):
        out = self.setup()
        subdirectory = "subdir"
        self.create_directory(subdirectory)
        os.chdir(subdirectory)
        Cd().execute([".."], out)
        expected_path = str(self.temp_path)
        # use Pwd to check the current working directory
        out2 = []
        Pwd().execute([], out2)
        self.assertEqual(expected_path + "\n", out2[0])
        self.teardown()

    def test_cd_up_multiple_directories(self):
        out = self.setup()
        subdirectory = "subdir"
        self.create_directory(subdirectory)
        os.chdir(subdirectory)
        Cd().execute(["../.."], out)
        expected_path = str(self.temp_path.parent)
        # use Pwd to check the current working directory
        out2 = []
        Pwd().execute([], out2)
        self.assertEqual(expected_path + "\n", out2[0])
        self.teardown()

    def test_cd_relative_path(self):
        out = self.setup()
        subdirectory = "subdir"
        self.create_directory(subdirectory)
        Cd().execute([f"./{subdirectory}"], out)
        expected_path = str(self.temp_path / subdirectory)
        # use Pwd to check the current working directory
        out2 = []
        Pwd().execute([], out2)
        self.assertEqual(expected_path + "\n", out2[0])
        self.teardown()

    def test_cd_absolute_path(self):
        out = self.setup()
        subdirectory = "subdir"
        self.create_directory(subdirectory)
        Cd().execute([f"{self.temp_path}/{subdirectory}"], out)
        expected_path = str(self.temp_path / subdirectory)
        # use Pwd to check the current working directory
        out2 = []
        Pwd().execute([], out2)
        self.assertEqual(expected_path + "\n", out2[0])
        self.teardown()

    def test_cd_relative_path_with_parent_directory(self):
        out = self.setup()
        subdirectory = "subdir"
        self.create_directory(subdirectory)
        os.chdir(self.temp_path)
        Cd().execute(["./subdir/.."], out)
        expected_path = str(self.temp_path)
        out2 = []
        Pwd().execute([], out2)
        self.assertEqual(expected_path + "\n", out2[0])
        self.teardown()

    def test_cd_to_root_directory(self):
        out = self.setup()
        subdirectory = "subdir"
        self.create_directory(subdirectory)
        os.chdir(subdirectory)
        Cd().execute(["/"], out)
        expected_path = "/"
        out2 = []
        Pwd().execute([], out2)
        self.assertEqual(expected_path + "\n", out2[0])
        self.teardown()

    def test_cd_multiple_commands(self):
        out = self.setup()
        subdirectory1 = "subdir1"
        self.create_directory(subdirectory1)
        os.chdir(subdirectory1)
        subdirectory2 = "subdir2"
        self.create_directory(subdirectory2)
        os.chdir(self.temp_path)
        Cd().execute([subdirectory1], out)
        Cd().execute([subdirectory2], out)
        expected_path = str(self.temp_path / subdirectory1 / subdirectory2)
        out2 = []
        Pwd().execute([], out2)
        self.assertEqual(expected_path + "\n", out2[0])
        self.teardown()

    def test_cd_invalid(self):
        out = self.setup()
        with self.assertRaises(DirectoryError):
            Cd().execute(["invalid"], out)
        self.teardown()
