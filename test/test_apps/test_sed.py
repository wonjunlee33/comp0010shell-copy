import tempfile
import unittest
from unittest.mock import patch
from pathlib import Path
from apps.sed import Sed
from error import ArgumentError, FileError


class TestSed(unittest.TestCase):
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

    def read_file_content(self, file_path):
        with open(file_path, "r") as f:
            return f.read()

    def test_sed_replace_pattern_in_file(self):
        expected_output = "Hello, Universe!"
        out = self.setup(["Hello, World!"])
        Sed().execute(["s/World/Universe/", self.test_file[0]], out)
        self.assertEqual(
            expected_output, self.read_file_content(self.test_file[0])
        )
        self.teardown()

    def test_sed_replace_pattern_in_file_without_flags(self):
        out = self.setup(["Hello, World! World!"])
        Sed().execute(["s/World/Universe/", self.test_file[0]], out)
        self.assertEqual(
            self.read_file_content(self.test_file[0]),
            "Hello, Universe! World!",
        )
        self.teardown()

    def test_sed_replace_pattern_in_file_with_flags(self):
        out = self.setup(["Hello, World! World! World!"])
        Sed().execute(["s/World/Universe/g", self.test_file[0]], out)
        self.assertEqual(
            self.read_file_content(self.test_file[0]),
            "Hello, Universe! Universe! Universe!",
        )
        self.teardown()

    def test_sed_replace_pattern_with_flags(self):
        out = self.setup(["Hello, World! World!"])
        expected_output = "Hello, Universe! Universe!"
        Sed().execute(["s/World/Universe/g", self.test_file[0]], out)
        self.assertEqual(
            expected_output, self.read_file_content(self.test_file[0])
        )
        self.teardown()

    def test_sed_nonexistent_file(self):
        out = self.setup(["Hello, World!"])
        with self.assertRaises(FileError):
            Sed().execute(["s/World/Universe/", "nonexistent_file.txt"], out)
        self.teardown()

    def test_sed_replace_pattern_from_stdin(self):
        out = self.setup(["Hello, World! World! 0"])
        expected_output = "Hello, Universe! World! 0\n"
        with patch("sys.stdin", open(self.test_file[0])):
            Sed().execute(["s/World/Universe/", self.test_file[0]], out)
        self.assertEqual(expected_output, "".join(out))
        self.teardown()

    def test_sed_replace_pattern_from_stdin_with_flags(self):
        out = self.setup(["Hello, World! 0\nHello, World! 1"])
        expected_output = "Hello, Universe! 0\nHello, Universe! 1\n"
        with patch("sys.stdin", open(self.test_file[0])):
            Sed().execute(["s/World/Universe/g"], out)
        self.assertEqual(expected_output, "".join(out))
        self.teardown()

    def test_sed_print_to_stdout(self):
        out = self.setup(["Hello, World!"])
        expected_output = "Hello, Universe!\n"
        Sed().execute(["s/World/Universe/", self.test_file[0]], out)
        self.assertEqual(expected_output, "".join(out))
        self.teardown()

    def test_sed_print_to_stdout_multiple_lines(self):
        out = self.setup(["Hello, World!\nHello, World!"])
        expected_output = "Hello, Universe!\nHello, Universe!\n"
        Sed().execute(["s/World/Universe/g", self.test_file[0]], out)
        self.assertEqual(expected_output, "".join(out))
        self.teardown()

    def test_sed_wrong_number_of_arguments(self):
        out = self.setup(["Hello, World!", "Barflesnarp"])
        with self.assertRaises(ArgumentError):
            Sed().execute(
                ["s/World/Universe/", self.test_file[0], self.test_file[1]],
                out,
            )
        self.teardown()

    def test_sed_exisiting_newline_at_end_stdin(self):
        out = self.setup(["Hello, World!\n"])
        expected_output = "Hello, Universe!\n"
        with patch("sys.stdin", open(self.test_file[0])):
            Sed().execute(["s/World/Universe/"], out)
        self.assertEqual(expected_output, "".join(out))
        self.teardown()

    def test_sed_exisiting_newline_at_end_file(self):
        out = self.setup(["Hello, World!\n"])
        expected_output = "Hello, Universe!\n"
        Sed().execute(["s/World/Universe/", self.test_file[0]], out)
        self.assertEqual(expected_output, "".join(out))
        self.teardown()

    def test_sed_regex_error_stdin(self):
        out = self.setup(["Hello, World!\n"])
        with self.assertRaises(ArgumentError):
            with patch("sys.stdin", open(self.test_file[0])):
                Sed().execute(["ashdahsdhsa"], out)
        self.teardown()

    def test_sed_regex_error_file(self):
        out = self.setup(["Hello, World!\n"])
        with self.assertRaises(ArgumentError):
            Sed().execute(["ashdahsdhsa", self.test_file[0]], out)
        self.teardown()

    def test_sed_no_stdin(self):
        out = self.setup([""])
        with self.assertRaises(ArgumentError):
            with patch("sys.stdin", open(self.test_file[0])):
                Sed().execute(["ashdahsdhsa"], out)
        self.teardown()
