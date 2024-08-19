import tempfile
import unittest
from pathlib import Path
from apps.head import Head
from unittest.mock import patch
from error import ArgumentError, FlagError, FileError
from hypothesis import given, strategies as st


class TestHead(unittest.TestCase):
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

    def test_head(self):
        out = self.setup(
            ["AAA\nBBB\nCCC\nDDD\nEEE\nFFF\nGGG\nHHH\nIII\nJJJ\n"]
        )
        expected_output = "AAA\nBBB\n"
        Head().execute(["-n", "2", self.test_file[0]], out)
        self.assertEqual(expected_output, "".join(out))
        self.teardown()

    def test_head_no_number(self):
        out = self.setup(["1\n2\n3\n4\n5\n6\n7\n8\n9\n10\n11\n12\n"])
        expected_output = "1\n2\n3\n4\n5\n6\n7\n8\n9\n10\n"
        Head().execute([self.test_file[0]], out)
        self.assertEqual(expected_output, "".join(out))
        self.teardown()

    def test_head_empty_file(self):
        out = self.setup([""])
        expected_output = ""
        Head().execute([self.test_file[0]], out)
        self.assertEqual(expected_output, "".join(out))
        self.teardown()

    def test_head_out_of_range(self):
        out = self.setup(["1\n2\n3\n4\n5\n6\n7\n8\n9\n10\n"])
        expected_output = "1\n2\n3\n4\n5\n6\n7\n8\n9\n10\n"
        Head().execute(["-n", "20", self.test_file[0]], out)
        self.assertEqual(expected_output, "".join(out))
        self.teardown()

    def test_head_wrong_flags(self):
        out = self.setup(
            ["AAA\nBBB\nCCC\nDDD\nEEE\nFFF\nGGG\nHHH\nIII\nJJJ\n"]
        )
        with self.assertRaises(FlagError):
            Head().execute(["-x", "2", self.test_file[0]], out)
        self.teardown()

    def test_head_too_many_args(self):
        out = self.setup(
            ["AAA\nBBB\nCCC\nDDD\nEEE\nFFF\nGGG\nHHH\nIII\nJJJ\n"]
        )
        with self.assertRaises(ArgumentError):
            Head().execute(["-n", "2", self.test_file[0], "10"], out)
        self.teardown()

    def test_head_two_args(self):
        out = self.setup(
            ["AAA\nBBB\nCCC\nDDD\nEEE\nFFF\nGGG\nHHH\nIII\nJJJ\n"]
        )
        expected_output = "AAA\nBBB\n"
        with patch("sys.stdin", open(self.test_file[0])):
            Head().execute(["-n", "2"], out)
        self.assertEqual(expected_output, "".join(out))
        self.teardown()

    def test_head_two_args_wrong_flags(self):
        out = self.setup(
            ["AAA\nBBB\nCCC\nDDD\nEEE\nFFF\nGGG\nHHH\nIII\nJJJ\n"]
        )
        with self.assertRaises(FlagError):
            with patch("sys.stdin", open(self.test_file[0])):
                Head().execute(["2", "-n"], out)
        self.teardown()

    def test_head_stdin(self):
        out = self.setup(["1\n2\n3\n4\n5\n6\n7\n8\n9\n10\n11\n12\n"])
        expected_output = "1\n2\n3\n4\n5\n6\n7\n8\n9\n10\n"
        with patch("sys.stdin", open(self.test_file[0])):
            Head().execute([], out)
        self.assertEqual(expected_output, "".join(out))
        self.teardown()

    def test_head_invalid_file(self):
        out = self.setup(["1\n2\n3\n4\n5\n6\n7\n8\n9\n10\n11\n12\n"])
        with self.assertRaises(FileError):
            Head().execute(["invalid_file"], out)
        self.teardown()

    # Hypothesis Testing
    # Length of output should be less than or equal to n
    @given(
        st.lists(
            st.text(
                alphabet=st.characters(
                    whitelist_categories=("Ll", "Lu", "Nd"),
                ),
                min_size=1,
            ),
        ),
        st.integers(min_value=1, max_value=100),
    )
    def test_hypothesis_length(self, contents, n):
        out = self.setup(["\n".join(contents) + "\n"])
        Head().execute(["-n", f"{n}", self.test_file[0]], out)
        self.assertLessEqual(len(out), n)
        self.teardown()
