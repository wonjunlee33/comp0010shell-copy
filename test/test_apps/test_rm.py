import unittest
import os
import tempfile
from hypothesis import given, strategies as st
from apps.rm import Rm
from error import ArgumentError, FileError, DirectoryError


class TestRm(unittest.TestCase):
    @classmethod
    def setup(self, files=None, directories=None):
        self.test_dir = tempfile.TemporaryDirectory()
        self.temp_path = self.test_dir.name

        if files:
            for file in files:
                with open(os.path.join(self.temp_path, file), "w") as f:
                    f.write("")

        if directories:
            for directory in directories:
                os.mkdir(os.path.join(self.temp_path, directory))

        os.chdir(self.temp_path)
        return []

    @classmethod
    def teardown(self):
        self.test_dir.cleanup()

    def test_rm_single_file(self):
        out = self.setup(["file1.txt"])
        Rm().execute(["file1.txt"], out)
        self.assertFalse(os.path.exists("file1.txt"))
        self.teardown()

    def test_rm_wrong_number_of_arguments(self):
        out = self.setup(["file1.txt", "file2.txt"])
        with self.assertRaises(ArgumentError):
            Rm().execute(["file1.txt", "file2.txt"], out)
        self.teardown()

    def test_rm_nonexistent_file(self):
        out = self.setup()
        with self.assertRaises(FileError):
            Rm().execute(["nonexistent_file.txt"], out)
        self.teardown()

    def test_rm_directory(self):
        out = self.setup(None, ["directory1"])
        with self.assertRaises(DirectoryError):
            Rm().execute(["directory1"], out)
        self.teardown()

    # Hypothesis Testing
    # removed directory must have less files than before
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
    def test_rm_less_file_in_directory_invariant(self, contents):
        if len(set(contents)) != len(contents):
            return
        contents = [os.path.join(content + ".txt") for content in contents]
        out = self.setup(contents)
        Rm().execute([contents[0]], out)
        self.assertLessEqual(len(os.listdir(".")), len(contents))
        self.teardown()
