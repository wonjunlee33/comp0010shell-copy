import tempfile
import unittest
from pathlib import Path
from apps.tail import Tail
from unittest.mock import patch
from error import ArgumentError, FlagError, FileError
from hypothesis import given, strategies as st


class TestTail(unittest.TestCase):
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

    def test_tail(self):
        out = self.setup(
            ["AAA\nBBB\nCCC\nDDD\nEEE\nFFF\nGGG\nHHH\nIII\nJJJ\n"]
        )
        expected_output = "III\nJJJ\n"
        Tail().execute(["-n", "2", self.test_file[0]], out)
        self.assertEqual(expected_output, "".join(out))
        self.teardown()

    def test_tail_no_number(self):
        out = self.setup(["1\n2\n3\n4\n5\n6\n7\n8\n9\n10\n11\n12\n"])
        expected_output = "3\n4\n5\n6\n7\n8\n9\n10\n11\n12\n"
        Tail().execute([self.test_file[0]], out)
        self.assertEqual(expected_output, "".join(out))
        self.teardown()

    def test_tail_empty_file(self):
        out = self.setup([""])
        expected_output = ""
        Tail().execute([self.test_file[0]], out)
        self.assertEqual(expected_output, "".join(out))
        self.teardown()

    def test_tail_out_of_range(self):
        out = self.setup(["1\n2\n3\n4\n5\n6\n7\n8\n9\n10\n"])
        expected_output = "1\n2\n3\n4\n5\n6\n7\n8\n9\n10\n"
        Tail().execute(["-n", "20", self.test_file[0]], out)
        self.assertEqual(expected_output, "".join(out))
        self.teardown()

    def test_tail_wrong_flags(self):
        out = self.setup(["a\nb\nc\nd\ne\nf\ng\nh\ni\nj\n"])
        with self.assertRaises(FlagError):
            Tail().execute(["-c", "16", self.test_file[0]], out)
        self.teardown()

    def test_tail_wrong_flags_2(self):
        out = self.setup(["a\nb\nc\nd\ne\nf\ng\nh\ni\nj\n"])
        with self.assertRaises(FlagError):
            Tail().execute(["-c", "hello", self.test_file[0]], out)
        self.teardown()

    def test_tail_too_many_args(self):
        out = self.setup(
            ["AAA\nBBB\nCCC\nDDD\nEEE\nFFF\nGGG\nHHH\nIII\nJJJ\n"]
        )
        with self.assertRaises(ArgumentError):
            Tail().execute(["-n", "2", self.test_file[0], "10"], out)
        self.teardown()

    def test_tail_two_args(self):
        out = self.setup(
            ["AAA\nBBB\nCCC\nDDD\nEEE\nFFF\nGGG\nHHH\nIII\nJJJ\n"]
        )
        expected_output = "III\nJJJ\n"
        with patch("sys.stdin", open(self.test_file[0])):
            Tail().execute(["-n", "2"], out)
        self.assertEqual(expected_output, "".join(out))
        self.teardown()

    def test_tail_two_args_wrong_flags(self):
        out = self.setup(
            ["AAA\nBBB\nCCC\nDDD\nEEE\nFFF\nGGG\nHHH\nIII\nJJJ\n"]
        )
        with self.assertRaises(FlagError):
            with patch("sys.stdin", open(self.test_file[0])):
                Tail().execute(["2", "-n"], out)
        self.teardown()

    def test_tail_stdin(self):
        out = self.setup(["1\n2\n3\n4\n5\n6\n7\n8\n9\n10\n11\n12\n"])
        expected_output = "3\n4\n5\n6\n7\n8\n9\n10\n11\n12\n"
        with patch("sys.stdin", open(self.test_file[0])):
            Tail().execute([], out)
        self.assertEqual(expected_output, "".join(out))
        self.teardown()

    def test_tail_invalid_file(self):
        out = self.setup(["1\n2\n3\n4\n5\n6\n7\n8\n9\n10\n11\n12\n"])
        with self.assertRaises(FileError):
            Tail().execute(["-n", "2", "invalid_file"], out)
        self.teardown()

    # Hypothesis tests
    # Length of output property testing
    @given(
        st.lists(
            st.text(
                min_size=1,
                alphabet=st.characters(
                    whitelist_categories=("Ll", "Lu", "Nd"),
                ),
            ),
            min_size=1,
        ),
        st.integers(min_value=1, max_value=100),
    )
    def test_hypothesis_length(self, contents, n):
        out = self.setup(["\n".join(contents) + "\n"])
        Tail().execute(["-n", f"{n}", self.test_file[0]], out)
        self.assertLessEqual(len(out), n)
        self.teardown()
