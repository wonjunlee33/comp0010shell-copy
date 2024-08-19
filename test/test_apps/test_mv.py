import unittest
import os
import tempfile
from hypothesis import given, strategies as st
from apps.mv import Mv
from error import ArgumentError, FileError


class TestMv(unittest.TestCase):
    @classmethod
    def setup(self, contents=None):
        self.test_dir = tempfile.TemporaryDirectory()
        self.temp_path = self.test_dir.name

        for content in contents:
            directory_path = os.path.join(
                self.temp_path, os.path.dirname(content)
            )
            os.makedirs(directory_path, exist_ok=True)
            with open(os.path.join(self.temp_path, content), "w") as f:
                f.write("")

        os.chdir(self.temp_path)
        return []

    @classmethod
    def teardown(self):
        self.test_dir.cleanup()

    def test_mv_single_file(self):
        out = self.setup(["source.txt"])
        destination_file = "destination.txt"
        Mv().execute(["source.txt", destination_file], out)
        self.assertTrue(os.path.isfile(destination_file))
        self.assertFalse(os.path.isfile("source.txt"))
        self.teardown()

    def test_mv_directory(self):
        out = self.setup(
            ["source_directory/file1.txt", "source_directory/file2.txt"]
        )
        os.mkdir("destination_directory")
        Mv().execute(["source_directory", "destination_directory"], out)
        self.assertTrue(os.path.isdir("destination_directory"))
        self.assertTrue(
            os.path.isfile(
                os.path.join(
                    "destination_directory/source_directory", "file1.txt"
                )
            )
        )
        self.assertTrue(
            os.path.isfile(
                os.path.join(
                    "destination_directory/source_directory", "file2.txt"
                )
            )
        )
        self.assertFalse(os.path.exists("source_directory"))
        self.teardown()

    def test_mv_directory_and_files(self):
        out = self.setup(
            [
                "source_directory/subdir/file1.txt",
                "source_directory/subdir/file2.txt",
                "source_directory/file3.txt",
            ]
        )
        os.mkdir("destination_directory")
        Mv().execute(["source_directory", "destination_directory"], out)
        self.assertTrue(os.path.isdir("destination_directory"))
        self.assertTrue(
            os.path.isfile(
                os.path.join(
                    "destination_directory/source_directory/subdir",
                    "file1.txt",
                )
            )
        )
        self.assertTrue(
            os.path.isfile(
                os.path.join(
                    "destination_directory/source_directory/subdir",
                    "file2.txt",
                )
            )
        )
        self.assertTrue(
            os.path.isfile("destination_directory/source_directory/file3.txt")
        )
        self.assertFalse(os.path.exists("source_directory"))
        self.teardown()

    def test_mv_force_overwrite(self):
        out = self.setup(["source.txt", "destination.txt"])
        Mv().execute(["-f", "source.txt", "destination.txt"], out)
        self.assertTrue(os.path.isfile("destination.txt"))
        self.assertFalse(os.path.isfile("source.txt"))
        self.teardown()

    def test_mv_to_same_directory(self):
        out = self.setup(["file1.txt"])
        Mv().execute(["file1.txt", "."], out)
        self.assertTrue(os.path.isfile("file1.txt"))
        self.teardown()

    def test_mv_source_file_does_not_exist(self):
        out = self.setup(["destination.txt"])
        with self.assertRaises(FileError):
            Mv().execute(["source.txt", "destination.txt"], out)
        self.teardown()

    def test_mv_destination_file_does_not_exist(self):
        out = self.setup(["source.txt"])
        Mv().execute(["-f", "source.txt", "destination.txt"], out)
        with self.assertRaises(FileError):
            Mv().execute(["source.txt", "destination.txt"], out)
        self.teardown()

    def test_mv_error_when_not_force_overwrite(self):
        out = self.setup(["source.txt", "destination.txt"])
        with self.assertRaises(FileError):
            Mv().execute(["source.txt", "destination.txt"], out)
        self.teardown()

    def test_mv_empty_directory(self):
        out = self.setup(["empty_directory"])
        os.mkdir("new_directory")
        Mv().execute(["empty_directory", "new_directory"], out)
        self.assertTrue(os.path.isdir("new_directory"))
        self.assertFalse(os.path.exists("empty_directory"))
        self.teardown()

    def test_mv_wrong_arguments(self):
        out = self.setup(["i.txt", "hate.txt", "this.txt"])
        with self.assertRaises(ArgumentError):
            Mv().execute(["-f"], out)
        self.teardown()

    # Hypothesis Testing
    # moved file directory has less files testing
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
    def test_mv_count_files(self, contents):
        contents = [
            os.path.join("source_directory", content + ".txt")
            for content in contents
        ]
        out = self.setup(contents)
        os.mkdir("destination_directory")
        Mv().execute([contents[0], "destination_directory/hello.txt"], out)
        self.assertGreaterEqual(
            len(contents), len(os.listdir("source_directory"))
        )
        self.teardown()
