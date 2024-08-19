import tempfile
import unittest
from hypothesis import given, strategies as st
from unittest.mock import patch
from pathlib import Path
from apps.cat import Cat
from error import FileError


class TestCat(unittest.TestCase):
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

    def test_cat(self):
        out = self.setup(
            ["AAA\nBBB\nCCC\nDDD\nEEE\nFFF\nGGG\nHHH\nIII\nJJJ\n"]
        )
        expected_output = "AAA\nBBB\nCCC\nDDD\nEEE\nFFF\nGGG\nHHH\nIII\nJJJ\n"
        Cat().execute([self.test_file[0]], out)
        self.assertEqual(expected_output, "".join(out))
        self.teardown()

    def test_cat_multiple_files(self):
        out = self.setup(["AAA", "CCC\n"])
        expected_output = "AAACCC\n"
        Cat().execute([self.test_file[0], self.test_file[1]], out)
        self.assertEqual(expected_output, "".join(out))
        self.teardown()

    def test_cat_newline(self):
        out = self.setup(["AAA\n"])
        Cat().execute([self.test_file[0]], out)
        self.assertEqual("AAA\n", "".join(out))
        self.teardown()

    def test_cat_no_newline(self):
        out = self.setup(["AAA"])
        Cat().execute([self.test_file[0]], out)
        self.assertEqual("AAA\n", "".join(out))
        self.teardown()

    def test_cat_multiple_files_newline(self):
        out = self.setup(["AAA\nBBB\n", "CCC\nDDD\n"])
        expected_output = "AAA\nBBB\nCCC\nDDD\n"
        Cat().execute([self.test_file[0], self.test_file[1]], out)
        self.assertEqual(expected_output, "".join(out))
        self.teardown()

    def test_cat_file_no_newline(self):
        out = self.setup(["AAA\nBBB"])
        expected_output = "AAA\nBBB\n"
        Cat().execute([self.test_file[0]], out)
        self.assertEqual(expected_output, "".join(out))
        self.teardown()

    def test_cat_non_existent_file(self):
        out = self.setup(
            ["AAA\nBBB\nCCC\nDDD\nEEE\nFFF\nGGG\nHHH\nIII\nJJJ\n"]
        )
        with self.assertRaises(FileError):
            Cat().execute(["Invalidfile.txt"], out)
        self.teardown()

    def test_cat_stdin(self):
        out = self.setup(
            ["AAA\nBBB\nCCC\nDDD\nEEE\nFFF\nGGG\nHHH\nIII\nJJJ\n"]
        )
        expected_output = "AAA\nBBB\nCCC\nDDD\nEEE\nFFF\nGGG\nHHH\nIII\nJJJ\n"
        with patch("sys.stdin", open(self.test_file[0])):
            Cat().execute([], out)
        self.assertEqual(expected_output, "".join(out))
        self.teardown()

    def test_cat_special_characters(self):
        out = self.setup(["$%^&*\n@#!\n"])
        expected_output = "$%^&*\n@#!\n"
        Cat().execute([self.test_file[0]], out)
        self.assertEqual(expected_output, "".join(out))
        self.teardown()

    def test_cat_multiple_files_order(self):
        out = self.setup(["AAA\n", "BBB\n", "CCC\n"])
        expected_output = "AAA\nBBB\nCCC\n"
        Cat().execute(
            [self.test_file[0], self.test_file[1], self.test_file[2]], out
        )
        self.assertEqual(expected_output, "".join(out))
        self.teardown()

    def test_cat_empty_file(self):
        out = self.setup([""])
        expected_output = ""
        Cat().execute([self.test_file[0]], out)
        self.assertEqual(expected_output, "".join(out))
        self.teardown()

    # Hypothesis tests
    # Chars in output >= input testing
    @given(
        st.lists(
            st.text(
                alphabet=st.characters(
                    whitelist_categories=("Ll", "Lu", "Nd"),
                ),
            ),
            min_size=2,
            max_size=2,
        ).filter(lambda lst: all(len(item) > 0 for item in lst)),
    )
    def test_cat_chars_less_than_invariant(self, contents):
        out = self.setup(contents)
        expected_output = len(contents[0])
        Cat().execute([self.test_file[0], self.test_file[1]], out)
        self.assertLessEqual(expected_output, len("".join(out)))
        self.teardown()

    # Chars in output == input testing
    @given(
        st.lists(
            st.text(
                alphabet=st.characters(
                    whitelist_categories=("Ll", "Lu", "Nd"),
                ),
            ),
            min_size=2,
            max_size=2,
        ).filter(lambda lst: all(len(item) > 0 for item in lst)),
    )
    def test_cat_chars_equal_invariant(self, contents):
        out = self.setup(contents)
        expected_output = len(contents[0]) + len(contents[1])
        Cat().execute([self.test_file[0], self.test_file[1]], out)
        self.assertLessEqual(expected_output, len("".join(out)))
        self.teardown()
