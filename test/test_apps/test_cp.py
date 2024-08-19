import unittest
import os
import tempfile
from hypothesis import given, strategies as st
from apps.cp import Cp
from error import DirectoryError, FileError, ArgumentError, FlagError


class TestCp(unittest.TestCase):
    @classmethod
    def setup(self):
        self.test_dir = tempfile.TemporaryDirectory()
        os.chdir(self.test_dir.name)
        return []

    @classmethod
    def create_file(self, filename, content=""):
        with open(filename, "w") as f:
            f.write(content)

    @classmethod
    def create_directory(self, dirname, contents=None):
        os.makedirs(dirname)
        if contents:
            for content in contents:
                content_path = os.path.join(dirname, content)
                if os.path.sep in content:
                    os.makedirs(os.path.dirname(content_path), exist_ok=True)
                with open(content_path, "w") as f:
                    f.write("")

    @classmethod
    def teardown(self):
        self.test_dir.cleanup()

    def test_cp_single_file(self):
        out = self.setup()
        source_file = "source.txt"
        destination_file = "destination.txt"
        self.create_file(source_file, "Hello, World!")
        Cp().execute([source_file, destination_file], out)
        self.assertTrue(os.path.isfile(destination_file))
        with open(destination_file, "r") as f:
            content = f.read()
        self.assertEqual("Hello, World!", content)
        self.teardown()

    def test_cp_nonexistent_file(self):
        out = self.setup()
        source_file = "source.txt"
        destination_file = "destination.txt"
        self.create_directory(destination_file)
        with self.assertRaises(FileError):
            Cp().execute([source_file, destination_file], out)
        self.teardown()

    def test_cp_copy_file_without_force(self):
        out = self.setup()
        source_file = "source.txt"
        destination_file = "destination.txt"
        self.create_file(source_file, "Source Content")
        self.create_file(destination_file, "Destination Content")
        with self.assertRaises(FileError):
            Cp().execute([source_file, destination_file], out)
        self.teardown()

    def test_cp_copy_directory_into_file(self):
        out = self.setup()
        source_directory = "source_directory"
        destination_file = "destination.txt"
        self.create_directory(source_directory)
        self.create_file(destination_file)
        with self.assertRaises(DirectoryError):
            Cp().execute(["-r", source_directory, destination_file], out)
        self.teardown()

    def test_cp_recursive_with_empty_directory(self):
        out = self.setup()
        source_directory = "source_directory"
        destination_directory = "destination_directory"
        self.create_directory(source_directory)
        Cp().execute(["-r", source_directory, destination_directory], out)
        self.assertTrue(os.path.isdir(destination_directory))
        self.teardown()

    def test_cp_recursive_with_contents(self):
        out = self.setup()
        source_directory = "source_directory"
        destination_directory = "destination_directory"
        contents = ["file1.txt", "file2.txt", "subdir/file3.txt"]
        self.create_directory(source_directory, contents)
        Cp().execute(["-r", source_directory, destination_directory], out)
        for content in contents:
            self.assertTrue(
                os.path.isfile(os.path.join(destination_directory, content))
            )
        self.teardown()

    def test_cp_directory(self):
        out = self.setup()
        source_directory = "source"
        destination_directory = "destination"
        os.makedirs(source_directory)
        file1_path = os.path.join(source_directory, "file1.txt")
        file2_path = os.path.join(source_directory, "file2.txt")
        self.create_file(file1_path)
        self.create_file(file2_path)
        Cp().execute(["-r", source_directory, destination_directory], out)
        destination_file1 = os.path.join(destination_directory, "file1.txt")
        destination_file2 = os.path.join(destination_directory, "file2.txt")
        self.assertTrue(os.path.isdir(destination_directory))
        self.assertTrue(os.path.isfile(destination_file1))
        self.assertTrue(os.path.isfile(destination_file2))
        self.teardown()

    def test_cp_force_overwrite(self):
        out = self.setup()
        source_file = "source.txt"
        destination_file = "destination.txt"
        self.create_file(source_file, "Source Content")
        self.create_file(destination_file, "Destination Content")
        Cp().execute(["-f", source_file, destination_file], out)
        with open(destination_file, "r") as f:
            content = f.read()
        self.assertEqual("Source Content", content)
        self.teardown()

    def test_cp_wrong_flag(self):
        out = self.setup()
        source_file = "source.txt"
        destination_file = "destination.txt"
        self.create_file(source_file, "Source Content")
        self.create_file(destination_file, "Destination Content")
        with self.assertRaises(FlagError):
            Cp().execute(["-x", source_file, destination_file], out)
        self.teardown()

    def test_cp_wrong_number_of_arguments(self):
        out = self.setup()
        source_file = "source.txt"
        destination_file = "destination.txt"
        self.create_file(source_file, "Source Content")
        self.create_file(destination_file, "Destination Content")
        with self.assertRaises(ArgumentError):
            Cp().execute([source_file], out)
        self.teardown()

    def test_cp_empty_file(self):
        out = self.setup()
        source_file = "source.txt"
        destination_file = "destination.txt"
        self.create_file(source_file)
        Cp().execute([source_file, destination_file], out)
        self.assertTrue(os.path.isfile(destination_file))
        with open(destination_file, "r") as f:
            content = f.read()
        self.assertEqual("", content)
        self.teardown()

    def test_cp_file_recursive(self):
        out = self.setup()
        source_file = "source.txt"
        destination_file = "destination.txt"
        self.create_file(source_file)
        with self.assertRaises(FileError):
            Cp().execute(["-r", source_file, destination_file], out)
        self.teardown()

    # Hypothesis Testing
    # Copied file existence testing
    @given(st.text())
    def test_cp_file_exists_invariant(self, content):
        out = self.setup()
        source_file = "source.txt"
        self.create_file(source_file, content)
        destination_file = "destination.txt"
        Cp().execute([source_file, destination_file], out)
        self.assertTrue(os.path.isfile(destination_file))
        self.teardown()

    # Copied file content equality testing
    @given(st.text())
    def test_cp_directory_content_invariant(self, content):
        out = self.setup()
        source_file = "source.txt"
        self.create_file(source_file, content)
        destination_file = "destination.txt"
        self.create_file(destination_file)
        Cp().execute(["-f", source_file, destination_file], out)
        with open(destination_file, "r") as f:
            destination_content = f.read()
        with open(source_file, "r") as f:
            source_content = f.read()
        self.assertEqual(source_content, destination_content)
        self.teardown()
