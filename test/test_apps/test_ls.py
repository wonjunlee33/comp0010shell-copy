import tempfile
import unittest
import os
from hypothesis import given, strategies as st
from pathlib import Path
from apps.ls import Ls
from error import ArgumentError, DirectoryError


class TestLs(unittest.TestCase):
    @classmethod
    def setup(self, contents=None):
        self.test_dir = tempfile.TemporaryDirectory()
        self.temp_path = Path(self.test_dir.name)
        for content in contents or []:
            with open(self.temp_path / content, "w") as f:
                f.write("")
        os.chdir(self.temp_path)
        return []

    @classmethod
    def teardown(self):
        self.test_dir.cleanup()

    def test_ls(self):
        out = self.setup(["file1", "file2", "dir1"])
        expected_output = {"dir1\n", "file1\n", "file2\n"}
        Ls().execute([], out)
        self.assertEqual(expected_output, set(out))
        self.teardown()

    def test_ls_specific_directory(self):
        out = self.setup(["file1", "file2"])
        os.mkdir("dir1")
        os.chdir(str(self.temp_path / "dir1"))
        os.mkdir("dir2")
        os.mkdir("dir3")
        os.chdir(str(self.temp_path))
        expected_output = {"dir2\n", "dir3\n"}
        Ls().execute(["dir1"], out)
        self.assertEqual(expected_output, set(out))
        self.teardown()

    def test_ls_wrong_arguments(self):
        out = self.setup()
        with self.assertRaises(ArgumentError):
            Ls().execute(["dir1", "dir2"], out)
        self.teardown()

    def test_ls_hidden_files(self):
        out = self.setup(["file1", ".file2"])
        expected_output = {"file1\n"}
        Ls().execute([], out)
        self.assertEqual(expected_output, set(out))
        self.teardown()

    def test_ls_wrong_directory(self):
        out = self.setup(["file1", "file2", "dir1"])
        with self.assertRaises(DirectoryError):
            Ls().execute(["invalid"], out)
        self.teardown()

    # Hypothesis Testing
    # ls dirs equal to actual number of dirs testing
    @given(
        st.lists(
            st.text(
                alphabet=st.characters(
                    whitelist_categories=("Ll", "Lu", "Nd"),
                ),
            ),
            min_size=1,
            max_size=10,
        ).filter(lambda lst: all(len(item) > 0 for item in lst))
    )
    def test_ls_number_of_dirs_invariant(self, directory_contents):
        if len(set(directory_contents)) != len(directory_contents):
            return
        out = self.setup(directory_contents)
        Ls().execute([], out)
        listed_items = len(out)
        num_actual_dirs = len(directory_contents)
        self.assertEqual(listed_items, num_actual_dirs)
        self.teardown()
