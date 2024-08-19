import unittest
from apps.echo import Echo
from hypothesis import given, strategies as st


class TestEcho(unittest.TestCase):
    @classmethod
    def setup(self):
        return []

    def test_echo(self):
        out = self.setup()
        Echo().execute(["foo"], out)
        self.assertEqual("".join(out), "foo\n")

    def test_echo_two(self):
        out = self.setup()
        Echo().execute(["hello", "world"], out)
        self.assertEqual("".join(out), "hello world\n")

    def test_echo_multi(self):
        out = self.setup()
        Echo().execute(["hello", "world", "echo", "foo"], out)
        self.assertEqual("".join(out), "hello world echo foo\n")

    def test_echo_numbers(self):
        out = self.setup()
        Echo().execute([str(i) for i in range(10)], out)
        self.assertEqual(
            "".join(out), " ".join([str(i) for i in range(10)]) + "\n"
        )

    def test_echo_keywords(self):
        out = self.setup()
        Echo().execute([";", "|", "'", '"', "`", "<", ">"], out)
        self.assertEqual("".join(out), "; | ' \" ` < >\n")

    def test_echo_special_characters(self):
        out = self.setup()
        Echo().execute(["!@#$%"], out)
        self.assertEqual("".join(out), "!@#$%\n")

    def test_echo_whitespace(self):
        out = self.setup()
        Echo().execute(["          "], out)
        self.assertEqual("".join(out), "          \n")

    def test_echo_newline(self):
        out = self.setup()
        Echo().execute(["Hello\nWorld"], out)
        self.assertEqual("".join(out), "Hello\nWorld\n")

    def test_echo_tabs(self):
        out = self.setup()
        Echo().execute(["Hello\tWorld"], out)
        self.assertEqual("".join(out), "Hello\tWorld\n")

    # Hypothesis Testing
    # Checking if the output has a whitespace for each argument
    @given(st.lists(st.text(min_size=1), min_size=1))
    def test_echo_hypothesis(self, args):
        out = self.setup()
        Echo().execute(args, out)
        self.assertEqual(len(out[0]), len("".join(args)) + len(args))
