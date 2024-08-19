import unittest
import os
import tempfile
from hypothesis import given, strategies as st
from apps.rmdir import Rmdir
from error import ArgumentError, FlagError, DirectoryError


class TestRmdir(unittest.TestCase):
    @classmethod
    def setup(self, directories=None):
        self.test_dir = tempfile.TemporaryDirectory()
        self.temp_path = self.test_dir.name

        if directories:
            for directory in directories:
                os.makedirs(os.path.join(self.temp_path, directory))

        os.chdir(self.temp_path)
        return []

    @classmethod
    def teardown(self):
        self.test_dir.cleanup()

    def test_rmdir_single_empty_directory(self):
        out = self.setup(directories=["empty_directory"])
        Rmdir().execute(["empty_directory"], out)
        self.assertFalse(os.path.exists("empty_directory"))
        self.teardown()

    def test_rmdir_nonexistent_directory(self):
        out = self.setup()
        with self.assertRaises(DirectoryError):
            Rmdir().execute(["nonexistent_directory"], out)
        self.teardown()

    def test_rmdir_nonempty_directory(self):
        out = self.setup(directories=["nonempty_directory/file1.txt"])
        with self.assertRaises(DirectoryError):
            Rmdir().execute(["nonempty_directory"], out)

    def test_rmdir_force_nonempty_directory(self):
        out = self.setup(directories=["nonempty_directory"])
        os.chdir("nonempty_directory")
        os.mkdir("subdirectory")
        open("file1.txt", "w").close()
        os.chdir("..")
        Rmdir().execute(["-r", "nonempty_directory"], out)
        self.assertFalse(os.path.exists("nonempty_directory"))
        self.teardown()

    def test_rmdir_force_nonexistent_directory(self):
        out = self.setup()
        with self.assertRaises(DirectoryError):
            Rmdir().execute(["-r", "nonexistent_directory"], out)
        self.teardown()

    def test_rmdir_wrong_number_of_arguments(self):
        out = self.setup(directories=["directory1", "directory2"])
        with self.assertRaises(ArgumentError):
            Rmdir().execute(["-r", "directory1", "directory2"], out)
        self.teardown()

    def test_rmdir_wrong_flags(self):
        out = self.setup(directories=["directory1"])
        with self.assertRaises(FlagError):
            Rmdir().execute(["-x", "directory1"], out)
        self.teardown()

    # Hypothesis Testing
    # removed directory must have less dirs than before
    @given(
        st.lists(
            st.text(
                alphabet=st.characters(
                    whitelist_categories=("Ll", "Lu", "Nd"),
                ),
            ),
            min_size=1,
            max_size=10,
        ).filter(lambda lst: all(len(item) > 0 for item in lst)),
    )
    def test_rmdir_less_file_in_directory_invariant(self, contents):
        if len(set(contents)) != len(contents):
            return
        out = self.setup(contents)
        expected_result = len(os.listdir("."))
        Rmdir().execute(["-r", contents[0]], out)
        self.assertFalse(os.path.exists(contents[0]))
        self.assertGreaterEqual(expected_result, len(os.listdir(".")))
        self.teardown()
