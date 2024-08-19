import tempfile
import unittest
from pathlib import Path
import os
from apps.find import Find
from error import ArgumentError, FlagError, DirectoryError


class TestFind(unittest.TestCase):
    @classmethod
    def setup(self, files):
        self.test_dir = tempfile.TemporaryDirectory()
        self.temp_path = Path(self.test_dir.name)
        os.chdir(self.temp_path)

        def create_subdirectories(path, files):
            for i in range(len(files)):
                if isinstance(files[i], list):
                    sub_dir = path / f"sub_dir_{i}"
                    sub_dir.mkdir()
                    create_subdirectories(sub_dir, files[i])
                else:
                    temp_path = str(path) + f"/{files[i]}"
                    with open(temp_path, "w") as f:
                        f.write("\n")

        create_subdirectories(self.temp_path, files)

        return []

    @classmethod
    def teardown(self):
        self.test_dir.cleanup()

    def test_find(self):
        out = self.setup(["a.txt", ["b.txt"]])
        Find().execute(["-name", "*"], out)
        expected_output = {"./a.txt\n", "./sub_dir_1\n", "./sub_dir_1/b.txt\n"}
        self.assertEqual(expected_output, set(out))
        self.teardown()

    def test_find_name(self):
        out = self.setup(["a.txt", ["b.txt"]])
        Find().execute(["-name", "a.txt"], out)
        expected_output = {"./a.txt\n"}
        self.assertEqual(expected_output, set(out))
        self.teardown()

    def test_find_many_sub_directories(self):
        out = self.setup(
            ["a.txt", ["b.txt", ["c.txt", ["d.txt", ["e.txt", ["f.txt"]]]]]]
        )
        Find().execute(["-name", "f.txt"], out)
        expected_output = {
            "./sub_dir_1/sub_dir_1/sub_dir_1/sub_dir_1/sub_dir_1/f.txt\n"
        }
        self.assertEqual(expected_output, set(out))
        self.teardown()

    def test_find_hidden_files(self):
        out = self.setup(["a.txt", [".b.txt"], "b.txt"])
        Find().execute(["-name", "b.txt"], out)
        expected_output = {"./b.txt\n"}
        self.assertEqual(expected_output, set(out))
        self.teardown()

    def test_find_hidden_file_in_dir(self):
        out = self.setup(["a.txt", [".b.txt"]])
        Find().execute(["-name", "sub_dir_1"], out)
        expected_output = {"./sub_dir_1\n"}
        self.assertEqual(expected_output, set(out))
        self.teardown()

    def test_not_find_hidden_file(self):
        out = self.setup(["a.txt", ".b.txt"])
        Find().execute(["-name", ".b.txt"], out)
        expected_output = set()
        self.assertEqual(expected_output, set(out))
        self.teardown()

    def test_find_path_name(self):
        out = self.setup(["a.txt", ["b.txt"]])
        Find().execute(["./", "-name", "a.txt"], out)
        expected_output = {"./a.txt\n"}
        self.assertEqual(expected_output, set(out))
        self.teardown()

    def test_find_dir_name(self):
        out = self.setup(["a.txt", ["b.txt"]])
        Find().execute(["./", "-name", "sub_dir_1"], out)
        expected_output = {"./sub_dir_1\n", "./sub_dir_1/b.txt\n"}
        self.assertEqual(expected_output, set(out))
        self.teardown()

    def test_find_invalid_flag(self):
        out = self.setup(["a.txt", ["b.txt"]])
        with self.assertRaises(FlagError):
            Find().execute(["./hello", "a.txt", "-name"], out)
        self.teardown()

    def test_find_invalid_dir(self):
        out = self.setup(["a.txt", ["b.txt"]])
        with self.assertRaises(DirectoryError):
            Find().execute(["./hello", "-name", "a.txt"], out)
        self.teardown()

    def test_find_no_args(self):
        out = self.setup(["a.txt", ["b.txt"]])
        with self.assertRaises(ArgumentError):
            Find().execute([], out)
        self.teardown()

    def test_find_no_flag(self):
        out = self.setup(["a.txt", ["b.txt"]])
        with self.assertRaises(FlagError):
            Find().execute(["a.txt"], out)
        self.teardown()

    def test_find_too_many_args(self):
        out = self.setup(["a.txt", ["b.txt"]])
        with self.assertRaises(ArgumentError):
            Find().execute(["-name", "a.txt", "b.txt", "c.txt"], out)
        self.teardown()

    def test_find_one_arg(self):
        out = self.setup(["a.txt", ["b.txt"]])
        with self.assertRaises(FlagError):
            Find().execute(["-name"], out)
        self.teardown()

    def test_find_one_arg_directory(self):
        out = self.setup(["a.txt", ["b.txt"]])
        with self.assertRaises(FlagError):
            Find().execute(["./", "-name"], out)
        self.teardown()
