import unittest
from apps.help import Help
from error import ArgumentError


class TestHelp(unittest.TestCase):
    def test_help(self):
        out = []
        expected_output = (
            """
    Usage 🚀:

        <command> [<args>] : Run one of the available commands.
        > <file> : Redirect output to a file.
        >> <file> : Append output to a file.
        < <file> : Use a file as input.
        <command> | <command> : Pipe output from one command to another.
        <command> ; <command> : Run multiple commands sequentially.

    The following commands are available 🤖:

        pwd, cd, echo, ls, ls, cat, head, tail, grep, sort, cut, find, \
uniq, mkdir, touch, rm, rmdir, mv, cp, color, font, sed, wc, exit

    Use <command> --help or <command> -h for more information about a command.
    """
            + "\n"
        )
        Help().execute([], out)
        self.assertEqual(expected_output, "".join(out))

    def test_help_too_many_args(self):
        out = []
        with self.assertRaises(ArgumentError):
            Help().execute(["-h", "-h"], out)
