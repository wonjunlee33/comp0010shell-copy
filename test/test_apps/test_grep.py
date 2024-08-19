import os
import tempfile
import unittest
from pathlib import Path
from apps.grep import Grep
from unittest.mock import patch
from error import ArgumentError, FileError


class TestGrep(unittest.TestCase):
    @classmethod
    def setup(self, contents):
        self.test_dir = tempfile.TemporaryDirectory()
        self.temp_path = Path(self.test_dir.name)
        self.test_file = []
        os.chdir(self.temp_path)

        for i in range(len(contents)):
            self.test_file.append(str(self.temp_path) + f"/test-{i}.txt")
            with open(self.test_file[i], "w") as f:
                f.write(contents[i])
        return []

    @classmethod
    def teardown(self):
        self.test_dir.cleanup()

    def test_grep(self):
        out = self.setup(
            ["AAA\nBBB\nCCC\nDDD\nEEE\nFFF\nGGG\nHHH\nIII\nJJJ\n"]
        )
        expected_output = "AAA\n"
        Grep().execute(["AAA", self.test_file[0]], out)
        self.assertEqual(expected_output, "".join(out))
        self.teardown()

    def test_grep_not(self):
        out = self.setup(
            ["AAA\nBBB\nCCC\nDDD\nEEE\nFFF\nGGG\nHHH\nIII\nJJJ\n"]
        )
        expected_output = "AAA\n"
        Grep().execute(["^A", self.test_file[0]], out)
        self.assertEqual(expected_output, "".join(out))
        self.teardown()

    def test_grep_character_set(self):
        out = self.setup(
            ["AAA\nBBB\nCCC\nDDD\nEEE\nFFF\nGGG\nHHH\nIII\nJJJ\n"]
        )
        expected_output = "AAA\nIII\n"
        Grep().execute(["[AI]", self.test_file[0]], out)
        self.assertEqual(expected_output, "".join(out))
        self.teardown()

    def test_grep_character_set_not(self):
        out = self.setup(
            ["AAA\nBBB\nCCC\nDDD\nEEE\nFFF\nGGG\nHHH\nIII\nJJJ\n"]
        )
        expected_output = "BBB\nCCC\nDDD\nEEE\nFFF\nGGG\nHHH\nJJJ\n"
        Grep().execute(["[^AI]", self.test_file[0]], out)
        self.assertEqual(expected_output, "".join(out))
        self.teardown()

    def test_grep_character_range(self):
        out = self.setup(
            ["AAA\nBBB\nCCC\nDDD\nEEE\nFFF\nGGG\nHHH\nIII\nJJJ\n"]
        )
        expected_output = "AAA\nBBB\nCCC\n"
        Grep().execute(["[A-C]", self.test_file[0]], out)
        self.assertEqual(expected_output, "".join(out))
        self.teardown()

    def test_grep_character_range_kleene(self):
        out = self.setup(
            ["AAA\nBBB\nCCC\nDDD\nEEE\nFFF\nGGG\nHHH\nIII\nJJJ\n"]
        )
        expected_output = "AAA\nBBB\nCCC\nDDD\nEEE\nFFF\nGGG\nHHH\nIII\nJJJ\n"
        Grep().execute(["[D-E]*", self.test_file[0]], out)
        self.assertEqual(expected_output, "".join(out))
        self.teardown()

    def test_grep_character_range_plus(self):
        out = self.setup(
            ["AAA\nBBB\nCCC\nDDD\nEEE\nFFF\nGGG\nHHH\nIII\nJJJ\n"]
        )
        expected_output = "DDD\nEEE\n"
        Grep().execute(["[D-E]+", self.test_file[0]], out)
        self.assertEqual(expected_output, "".join(out))
        self.teardown()

    def test_grep_character_range_question(self):
        out = self.setup(["ABCDEFG\nDEFGHIJ\nGHIJKLM\n"])
        expected_output = "DEFGHIJ\n"
        Grep().execute(["[D-E]", self.test_file[0]], out)
        self.assertEqual(expected_output, "".join(out))
        self.teardown()

    def test_grep_digits(self):
        out = self.setup(["123\nABC\n789\nABC123\n"])
        expected_output = "123\n789\n"
        Grep().execute(["[0-9]", self.test_file[0]], out)
        self.assertEqual(expected_output, "".join(out))
        self.teardown()

    def test_grep_empty_file(self):
        out = self.setup([""])
        expected_output = ""
        Grep().execute(["AAA", self.test_file[0]], out)
        self.assertEqual(expected_output, "".join(out))
        self.teardown()

    def test_grep_no_eol(self):
        out = self.setup(["AAA"])
        expected_output = "AAA\n"
        Grep().execute(["AAA", self.test_file[0]], out)
        self.assertEqual(expected_output, "".join(out))
        self.teardown()

    def test_grep_value_error(self):
        out = self.setup(
            ["AAA\nBBB\nCCC\nDDD\nEEE\nFFF\nGGG\nHHH\nIII\nJJJ\n"]
        )
        with self.assertRaises(ArgumentError):
            Grep().execute([], out)
        self.teardown()

    def test_grep_invalid_file(self):
        out = self.setup(
            ["AAA\nBBB\nCCC\nDDD\nEEE\nFFF\nGGG\nHHH\nIII\nJJJ\n"]
        )
        with self.assertRaises(FileError):
            Grep().execute(["AAA", "invalid_file"], out)
        self.teardown()

    def test_grep_stdin(self):
        out = self.setup(
            ["AAA\nBBB\nCCC\nDDD\nEEE\nFFF\nGGG\nHHH\nIII\nJJJ\n"]
        )
        expected_output = "AAA\n"
        with patch("sys.stdin", open(self.test_file[0])):
            Grep().execute(["AAA"], out)
        self.assertEqual(expected_output, "".join(out))
        self.teardown()

    def test_grep_multiple_files(self):
        out = self.setup(
            [
                "AAA\nBBB\nCCC\nDDD\nEEE\nFFF\nGGG\nHHH\nIII\nJJJ\n",
                "AAA\nBBB\nCCC\nDDD\nEEE\nFFF\nGGG\nHHH\nIII\nJJJ\n",
            ]
        )
        expected_output = (
            self.test_file[0] + ":AAA\n" + self.test_file[1] + ":AAA\n"
        )
        Grep().execute(["AAA", self.test_file[0], self.test_file[1]], out)
        self.assertEqual(expected_output, "".join(out))
        self.teardown()

    def test_grep_invalid_regex(self):
        out = self.setup(
            ["AAA\nBBB\nCCC\nDDD\nEEE\nFFF\nGGG\nHHH\nIII\nJJJ\n"]
        )
        with self.assertRaises(ArgumentError):
            Grep().execute(["[*", self.test_file[0]], out)
        self.teardown()
