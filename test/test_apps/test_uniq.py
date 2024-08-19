import tempfile
import unittest
from pathlib import Path
import sys
from apps.uniq import Uniq
from error import ArgumentError, FlagError, FileError
from hypothesis import given, strategies as st
from unittest.mock import patch


class TestUniq(unittest.TestCase):
    @classmethod
    def setup(self, contents):
        self.test_dir = tempfile.TemporaryDirectory()
        self.temp_path = Path(self.test_dir.name)
        self.test_file = []
        self.saved_stdin = sys.stdin
        for i in range(len(contents)):
            self.test_file.append(str(self.temp_path) + f"/test-{i}.txt")
            with open(self.test_file[i], "w") as f:
                f.write(contents[i])
        return []

    @classmethod
    def teardown(self):
        self.test_dir.cleanup()
        sys.stdin = self.saved_stdin

    def test_uniq(self):
        out = self.setup(["AAA\nAAA\nBBB\nBBB\nCCC\nCCC\n"])
        expected_output = "AAA\nBBB\nCCC\n"
        Uniq().execute([self.test_file[0]], out)
        self.assertEqual(expected_output, "".join(out))
        self.teardown()

    def test_uniq_2(self):
        out = self.setup(["AAA\naaa\nBBB\nbbb\nCCC\nccc\n"])
        expected_output = "AAA\naaa\nBBB\nbbb\nCCC\nccc\n"
        Uniq().execute([self.test_file[0]], out)
        self.assertEqual(expected_output, "".join(out))
        self.teardown()

    def test_uniq_lowercase(self):
        out = self.setup(["AAA\naaa\nBBB\nbbb\nCCC\nccc\n"])
        expected_output = "AAA\nBBB\nCCC\n"
        Uniq().execute(["-i", self.test_file[0]], out)
        self.assertEqual(expected_output, "".join(out))
        self.teardown()

    def test_uniq_lowercase_2(self):
        out = self.setup(["aaa\nAAA\nbbb\nBBB\nccc\nCCC\n"])
        expected_output = "aaa\nbbb\nccc\n"
        Uniq().execute(["-i", self.test_file[0]], out)
        self.assertEqual(expected_output, "".join(out))
        self.teardown()

    def test_uniq_long(self):
        out = self.setup(
            ["AAA\nAAA\nAAA\nAAA\nAAA\nAAA\nAAA\nAAA\nAAA\nAAA\n"]
        )
        expected_output = "AAA\n"
        Uniq().execute([self.test_file[0]], out)
        self.assertEqual(expected_output, "".join(out))
        self.teardown()

    def test_uniq_long_lowercase(self):
        out = self.setup(
            ["AAA\naaa\nAAA\naaa\nAAA\naaa\nAAA\naaa\nAAA\naaa\n"]
        )
        expected_output = "AAA\n"
        Uniq().execute(["-i", self.test_file[0]], out)
        self.assertEqual(expected_output, "".join(out))
        self.teardown()

    def test_uniq_stress(self):
        temp = [str(i) + "\n" for i in range(10000)]
        out = self.setup(["".join(temp)])
        expected_output = "".join(temp)
        Uniq().execute([self.test_file[0]], out)
        self.assertEqual(expected_output, "".join(out))
        self.teardown()

    def test_uniq_stress_2(self):
        temp = ["Foo\n" for i in range(10000)]
        out = self.setup(["".join(temp)])
        expected_output = "Foo\n"
        Uniq().execute([self.test_file[0]], out)
        self.assertEqual(expected_output, "".join(out))
        self.teardown()

    def test_uniq_wrong_flags_1(self):
        out = self.setup(["a", "b"])
        with self.assertRaises(FileError):
            Uniq().execute(["invalidfile.txt"], out)
        self.teardown()

    def test_uniq_wrong_flags_2(self):
        out = self.setup(["a"])
        with self.assertRaises(FlagError):
            Uniq().execute(["-x", self.test_file[0]], out)
        self.teardown()

    def test_uniq_wrong_flags_3(self):
        out = self.setup(["a", "b"])
        with self.assertRaises(ArgumentError):
            Uniq().execute(["-x", self.test_file[0], self.test_file[1]], out)
        self.teardown()

    def test_uniq_stdin(self):
        out = self.setup(["AAA\nAAA\nBBB\nBBB\nCCC\nCCC\n"])
        expected_output = "AAA\nBBB\nCCC\n"
        with patch("sys.stdin", open(self.test_file[0])):
            Uniq().execute([], out)
        self.assertEqual(expected_output, "".join(out))
        self.teardown()

    def test_uniq_2_stdin(self):
        out = self.setup(["AAA\naaa\nBBB\nbbb\nCCC\nccc\n"])
        expected_output = "AAA\naaa\nBBB\nbbb\nCCC\nccc\n"
        with patch("sys.stdin", open(self.test_file[0])):
            Uniq().execute([], out)
        self.assertEqual(expected_output, "".join(out))
        self.teardown()

    def test_uniq_lowercase_stdin(self):
        out = self.setup(["AAA\naaa\nBBB\nbbb\nCCC\nccc\n"])
        expected_output = "AAA\nBBB\nCCC\n"
        with patch("sys.stdin", open(self.test_file[0])):
            Uniq().execute(["-i"], out)
        self.assertEqual(expected_output, "".join(out))
        self.teardown()

    # Hypothesis tests
    # out must be shorter than contents
    @given(st.lists(st.text(min_size=1, alphabet="AaBbCc"), min_size=1))
    def test_uniq_hypothesis(self, contents):
        out = self.setup(["\n".join(contents) + "\n"])
        Uniq().execute(["-i", self.test_file[0]], out)
        self.assertLessEqual(len(out), len(contents))
        self.teardown()

    # out must be shorter than elements with flag
    @given(st.lists(st.text(min_size=1, alphabet="AaBbCc"), min_size=1))
    def test_uniq_hypothesis_ignore(self, contents):
        out = self.setup(["\n".join(contents) + "\n"])
        Uniq().execute([self.test_file[0]], out)
        self.assertLessEqual(len(out), len(contents))
        self.teardown()
