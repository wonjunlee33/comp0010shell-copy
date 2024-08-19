import tempfile
import unittest
from pathlib import Path
import sys
import io
from apps.cut import Cut
from parameterized import parameterized
from error import ArgumentError, FlagError, FileError
from hypothesis import given, strategies as st
from unittest.mock import patch


class TestCut(unittest.TestCase):
    @classmethod
    def setup(self, contents):
        self.test_dir = tempfile.TemporaryDirectory()
        self.temp_path = Path(self.test_dir.name)
        self.saved_stdin = sys.stdin
        self.test_file = []
        for i in range(len(contents)):
            self.test_file.append(str(self.temp_path) + f"/test-{i}.txt")
            with open(self.test_file[i], "w") as f:
                f.write(contents[i])
        return []

    @classmethod
    def teardown(self):
        self.test_dir.cleanup()
        sys.stdin = self.saved_stdin

    @parameterized.expand(
        # Testing define_ranges of Cut class
        [
            ("3", [["3", "3"]]),
            ("-3", [["1", "3"]]),
            ("4-", [["4", ""]]),
            ("1-3,3-", [["1", ""]]),
            ("2,3,2-", [["2", ""]]),
            ("4,8,6-", [["4", "4"], ["6", ""]]),
            ("-3,1-2,4", [["1", "3"], ["4", "4"]]),
            ("2,-3,4", [["1", "3"], ["4", "4"]]),
            ("-3,5-", [["1", "3"], ["5", ""]]),
            ("-3,3-", [["1", ""]]),
            ("1-,-2", [["1", ""]]),
            ("1-3,2-7", [["1", "7"]]),
            ("1-5,2-3", [["1", "5"]]),
        ]
    )
    def test_cut_ranges(self, args, expected):
        out = Cut().define_ranges(args)
        self.assertEqual(expected, out)

    def test_cut(self):
        out = self.setup(["ABCDEF\nBCDEFGHIJK\nABCDEF\n"])
        expected_output = "ACE\nBDF\nACE\n"
        Cut().execute(["-b", "1,3,5", self.test_file[0]], out)
        self.assertEqual(expected_output, "".join(out))

    def test_cut_range(self):
        out = self.setup(["ABCDEF\nBCDEFGHIJK\nABCDEF\n"])
        expected_output = "BCDE\nCDEF\nBCDE\n"
        Cut().execute(["-b", "2-5", self.test_file[0]], out)
        self.assertEqual(expected_output, "".join(out))

    def test_cut_wrong_flags(self):
        out = self.setup([])
        with self.assertRaises(ArgumentError):
            Cut().execute([], out)
        self.teardown()

    def test_cut_wrong_flags_2(self):
        out = self.setup([])
        with self.assertRaises(FlagError):
            Cut().execute(["-c"], out)
        self.teardown()

    def test_cut_wrong_flags_3(self):
        out = self.setup(["abc"])
        with self.assertRaises(ArgumentError):
            Cut().execute(["-c", "1,2,3", self.test_file[0], "2"], out)
        self.teardown()

    def test_cut_stdin(self):
        out = self.setup(["ABCDEF\nBCDEFGHIJK\nABCDEF\n"])
        expected_output = "ABCDEF\nBCDEFGHIJK\nABCDEF\n"
        with patch("sys.stdin", open(self.test_file[0])):
            Cut().execute(["-b", "1-3,3-"], out)
        self.assertEqual(expected_output, "".join(out))
        self.teardown()

    def test_cut_stdin_empty(self):
        out = self.setup([])
        sys.stdin = io.StringIO()
        with self.assertRaises(ArgumentError):
            Cut().execute(["-b", "1-3,3-"], out)
        self.teardown()

    def test_cut_invalid_file(self):
        out = self.setup(["a", "b"])
        with self.assertRaises(FileError):
            Cut().execute(["-b", "1-3", "invalidfile.txt"], out)
        self.teardown()

    # Hypothesis Testing
    # Range Property testing
    @given(
        st.text(min_size=1, max_size=100),
        st.integers(min_value=1, max_value=100),
        st.integers(min_value=1, max_value=100),
    )
    def test_cut_text(self, text, start, end):
        out = self.setup([text])
        check_start, check_end = sorted([start, end])
        Cut().execute(
            ["-b", f"{check_start}-{check_end}", self.test_file[0]], out
        )
        expected_output = min((check_end - check_start) + 1, len(text))
        self.assertLessEqual(len(out[0][:-1]), expected_output)
        self.teardown()

    # Subset Property testing
    @given(
        st.text(
            min_size=50,
            max_size=100,
            alphabet=st.characters(
                whitelist_categories=("Ll", "Lu", "Nd"),
            ),
        ),
        st.integers(min_value=1, max_value=100),
        st.integers(min_value=1, max_value=100),
    )
    def test_cut_contains(self, text, start, end):
        out = self.setup([text])
        check_start, check_end = sorted([start, end])
        Cut().execute(
            ["-b", f"{check_start}-{check_end}", self.test_file[0]], out
        )
        self.assertTrue(set(text).issuperset(set(out[0][:-1])))
        self.teardown()

    # Order Preservation
    @given(
        st.text(
            min_size=50,
            max_size=100,
            alphabet="abcdefghijklmnopqrstuvwxyz",
        ),
        st.lists(st.integers(min_value=1, max_value=100), min_size=1),
    )
    def test_cut_order(self, text, ranges):
        out = self.setup(["".join(sorted(text))])
        Cut().execute(
            ["-b", ",".join([str(i) for i in ranges]), self.test_file[0]], out
        )
        self.assertEqual(out[0][:-1], "".join(sorted(out[0][:-1])))
        self.teardown()
