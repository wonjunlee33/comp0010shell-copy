import tempfile
import unittest
from pathlib import Path
from call import Call
import io
from error import RedirectError, ApplicationError
from hypothesis import given, strategies as st


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
        Call(["cat", self.test_file[0]], [], [], [out])
        self.assertEqual(
            "AAA\nBBB\nCCC\nDDD\nEEE\nFFF\nGGG\nHHH\nIII\nJJJ\n", "".join(out)
        )
        self.teardown()

    def test_call_unsupported(self):
        out = self.setup(
            ["AAA\nBBB\nCCC\nDDD\nEEE\nFFF\nGGG\nHHH\nIII\nJJJ\n"]
        )
        with self.assertRaises(ApplicationError):
            Call(["unsupported", self.test_file[0]], [], [], [out])
        self.teardown()

    def test_redirect_stdin(self):
        out = self.setup(
            ["AAA\nAAA\nAAA\nAAA\nAAA\nAAA\nAAA\nAAA\nAAA\nAAA\n"]
        )
        Call(["uniq"], [self.test_file[0]], [], [out])
        self.assertEqual("AAA\n", "".join(out))
        self.teardown()

    def test_call_pipe(self):
        out = self.setup(["AAA\n"])
        expected_output = "AAA\n"
        Call(["cat"], [], [], [out], io.StringIO("AAA\n"))
        self.assertEqual(expected_output, "".join(out))
        self.teardown()

    def test_redirect_stdout(self):
        out = self.setup([""])
        Call(["echo", "Foo", "Bar"], [], [[self.test_file[0], "w"]], [out])
        with open(self.test_file[0], "r") as f:
            self.assertEqual("Foo Bar\n", f.read())
        self.teardown()

    def test_redirect_stdout_append(self):
        out = self.setup(["Hello\n"])
        Call(["echo", "Foo", "Bar"], [], [[self.test_file[0], "a"]], [out])
        with open(self.test_file[0], "r") as f:
            self.assertEqual("Hello\nFoo Bar\n", f.read())
        self.teardown()

    def test_redirect_too_many(self):
        out = self.setup(["AAA\n", "BBB\n"])
        with self.assertRaises(RedirectError):
            Call(["cat"], [self.test_file[0], self.test_file[1]], [], [out])
        self.teardown()

    def test_pipe_redirect(self):
        out = self.setup(["AAA\n"])
        with self.assertRaises(RedirectError):
            Call(["cat"], [self.test_file[0]], [], [out], io.StringIO("AAA\n"))
        self.teardown()

    def test_redirect_stdin_fail(self):
        out = self.setup(
            ["AAA\nAAA\nAAA\nAAA\nAAA\nAAA\nAAA\nAAA\nAAA\nAAA\n"]
        )
        with self.assertRaises(RedirectError):
            Call(["uniq"], ["nonexistent_file"], [], [out])
        self.teardown()

    # For all unknown strings, application should raise an error
    @given(
        st.text(min_size=1),
    )
    def test_call_unsupported_hypothesis(self, application):
        out = self.setup([])
        with self.assertRaises(ApplicationError):
            Call([application], [], [], [out], None)
        self.teardown()
