import unittest
import os
import tempfile
from hypothesis import given, strategies as st
from apps.mkdir import Mkdir
from error import ArgumentError, DirectoryError


class TestMkdir(unittest.TestCase):
    @classmethod
    def setup(self):
        self.test_dir = tempfile.TemporaryDirectory()
        os.chdir(self.test_dir.name)
        return []

    @classmethod
    def teardown(self):
        self.test_dir.cleanup()

    def test_mkdir_single_directory(self):
        out = self.setup()
        directory_name = "new_directory"
        expected_output = ""
        Mkdir().execute([directory_name], out)
        self.assertEqual(expected_output, "".join(out))
        self.assertTrue(os.path.isdir(directory_name))
        self.teardown()

    def test_mkdir_relative_path(self):
        out = self.setup()
        directory_name = "relative_directory"
        expected_output = ""
        Mkdir().execute(["./" + directory_name], out)
        self.assertEqual(expected_output, "".join(out))
        self.assertTrue(os.path.isdir(directory_name))
        self.teardown()

    def test_mkdir_absolute_path(self):
        out = self.setup()
        directory_name = "absolute_directory"
        absolute_path = os.path.join(self.test_dir.name, directory_name)
        expected_output = ""
        Mkdir().execute([absolute_path], out)
        self.assertEqual(expected_output, "".join(out))
        self.assertTrue(os.path.isdir(absolute_path))
        self.teardown()

    def test_mkdir_nested_directory(self):
        out = self.setup()
        os.mkdir("parent")
        nested_directory = "parent/child"
        expected_output = ""
        Mkdir().execute([nested_directory], out)
        self.assertEqual(expected_output, "".join(out))
        self.assertTrue(os.path.isdir(nested_directory))
        self.teardown()

    def test_mkdir_special_characters_directory(self):
        out = self.setup()
        special_characters_directory = "!@#$%^&*()_+-=[]{}"
        expected_output = ""
        Mkdir().execute([special_characters_directory], out)
        self.assertEqual(expected_output, "".join(out))
        self.assertTrue(os.path.isdir(special_characters_directory))
        self.teardown()

    def test_mkdir_unicode_directory(self):
        out = self.setup()
        unicode_directory = "紅太陽在天上"
        expected_output = ""
        Mkdir().execute([unicode_directory], out)
        self.assertEqual(expected_output, "".join(out))
        self.assertTrue(os.path.isdir(unicode_directory))
        self.teardown()

    def test_mkdir_wrong_arguments(self):
        out = self.setup()
        with self.assertRaises(ArgumentError):
            Mkdir().execute([], out)
        self.teardown()

    def test_mkdir_existing_directory(self):
        out = self.setup()
        directory_name = "existing_directory"
        os.mkdir(directory_name)
        with self.assertRaises(DirectoryError):
            Mkdir().execute([directory_name], out)
        self.teardown()

    # created directory must exist invariant
    @given(
        st.text(
            alphabet=st.characters(
                whitelist_categories=("Ll", "Lu", "Nd"),
            ),
        ),
    )
    def test_mkdir_unique_directory_names(self, directory_name):
        out = self.setup()
        if directory_name == "":
            return
        Mkdir().execute([directory_name], out)
        self.assertTrue(os.path.isdir(directory_name))
        self.teardown()

    # Hypothesis Testing
    # number of created dirs equal to actual number testing
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
    def test_mkdir_count_directory_names(self, directory_name):
        if len(set(directory_name)) != len(directory_name):
            return
        out = self.setup()
        for directory in directory_name:
            Mkdir().execute([directory], out)
        # compare number of directories created to actual number of directories
        self.assertEqual(len(directory_name), len(os.listdir()))
        self.teardown()
