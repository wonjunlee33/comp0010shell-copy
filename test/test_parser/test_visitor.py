import tempfile
import unittest
import os
from pathlib import Path
from shell import parse
from error import ArgumentError


class TestVisitor(unittest.TestCase):
    def setup(self, contents):
        self.test_dir = tempfile.TemporaryDirectory()
        self.temp_path = Path(self.test_dir.name)
        self.test_file = []
        for i in range(len(contents)):
            self.test_file.append(str(self.temp_path) + f"/test-{i}.txt")
            with open(self.test_file[i], "w") as f:
                f.write(contents[i])
        return []

    def teardown(self):
        self.test_dir.cleanup()

    def test_call(self):
        out = self.setup(
            ["AAA\nBBB\nCCC\nDDD\nEEE\nFFF\nGGG\nHHH\nIII\nJJJ\n"]
        )
        out = parse("cat " + self.test_file[0])
        self.assertEqual(
            "AAA\nBBB\nCCC\nDDD\nEEE\nFFF\nGGG\nHHH\nIII\nJJJ\n", "".join(out)
        )
        self.teardown()

    def test_redirection_stdin(self):
        out = self.setup(["ABCDEFFEDCBA\nABCDDCBA\n"])
        out = parse("cat < " + self.test_file[0])
        self.assertEqual("ABCDEFFEDCBA\nABCDDCBA\n", "".join(out))
        self.teardown()

    def test_redirection_stdin_space(self):
        out = self.setup(["ABCDEFFEDCBA\nABCDDCBA\n"])
        out = parse("cat <" + self.test_file[0])
        self.assertEqual("ABCDEFFEDCBA\nABCDDCBA\n", "".join(out))
        self.teardown()

    def test_redirection_stdout(self):
        self.setup([""])
        parse("echo foo > " + self.test_file[0])
        with open(self.test_file[0], "r") as f:
            self.assertEqual("foo\n", f.read())
        self.teardown()

    def test_redirection_stdout_append(self):
        self.setup(["ABCDEFFEDCBA\nABCDDCBA\n"])
        parse("echo ABCD >> " + self.test_file[0])
        with open(self.test_file[0], "r") as f:
            self.assertEqual("ABCDEFFEDCBA\nABCDDCBA\nABCD\n", f.read())
        self.teardown()

    def test_pipe(self):
        out = self.setup([])
        out = parse("echo foo | cat")
        self.assertEqual("foo\n", "".join(out))
        self.teardown()

    def test_argument_quoted_single(self):
        out = self.setup([])
        out = parse("echo 'foo bar'")
        self.assertEqual("foo bar\n", "".join(out))
        self.teardown()

    def test_argument_quoted_double(self):
        out = self.setup([])
        out = parse('echo "foo bar"')
        self.assertEqual("foo bar\n", "".join(out))
        self.teardown()

    def test_argument_quoted_backquote(self):
        out = self.setup([])
        out = parse("echo `echo foo`")
        self.assertEqual("foo\n", "".join(out))
        self.teardown()

    def test_argument_quoted_backquote_multiarg(self):
        out = self.setup(["ccc\naaa\nbbb\n"])
        out = parse("echo `sort " + self.test_file[0] + "`")
        self.assertEqual("aaa bbb ccc\n", "".join(out))
        self.teardown()

    def test_argument_quoted_backquote_multiarg2(self):
        out = self.setup([])
        out = parse('echo `echo foo   "  hello"`')
        self.assertEqual("foo hello\n", "".join(out))
        self.teardown()

    def test_argument_multi(self):
        out = self.setup([])
        out = parse("echo foo'bar'")
        self.assertEqual("foobar\n", "".join(out))
        self.teardown()

    def test_argument_multi_backquote(self):
        out = self.setup([])
        out = parse("echo foo`echo bar`'hello'")
        self.assertEqual("foobarhello\n", "".join(out))
        self.teardown()

    def test_quoted_double_backquote(self):
        out = self.setup([])
        out = parse('echo "`echo foo`"')
        self.assertEqual("foo\n", "".join(out))
        self.teardown()

    def test_quoted_double_backquote_multi(self):
        out = self.setup([])
        out = parse('echo "`echo foo`bar"')
        self.assertEqual("foobar\n", "".join(out))
        self.teardown()

    def test_argument_glob(self):
        out = self.setup(["a", "b"])
        os.chdir(self.temp_path)
        out = parse("echo *")
        result = set(out[0].split())
        self.assertEqual({f"test-{i}.txt" for i in range(2)}, result)
        self.teardown()

    def test_argument_glob_multi(self):
        out = self.setup(["a", "b", "c"])
        os.chdir(self.temp_path)
        out = parse("echo *'.txt'")
        result = set(out[0].split())
        self.assertEqual({f"test-{i}.txt" for i in range(3)}, result)
        self.teardown()

    def test_globbing_no_match(self):
        self.setup([])
        os.chdir(self.temp_path)
        with self.assertRaises(ArgumentError):
            parse("echo *")
        self.teardown()

    def test_no_subarg(self):
        out = self.setup([])
        os.chdir(self.temp_path)
        out = parse("echo `echo foo | cut -b 5`")
        self.assertEqual("\n", "".join(out))
        self.teardown()
