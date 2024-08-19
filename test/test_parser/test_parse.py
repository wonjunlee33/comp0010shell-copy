import unittest
from shell import parse
from parameterized import parameterized


class TestParse(unittest.TestCase):
    @parameterized.expand(
        # Testing Edge Cases
        [
            ('ec`echo "ho"` "hello"', "hello"),
            ('echo `echo "hello"`', "hello"),
            ('echo "hello `echo "hello"` hello"', "hello hello hello"),
            ('echo "hello `echo "bye"` hello"', "hello bye hello"),
            (
                'echo "hello `echo "bye"` hello `echo "bye"`"',
                "hello bye hello bye",
            ),
            ('echo "hello   foo bar"', "hello   foo bar"),
            ("echo `echo hello    foo`", "hello foo"),
            ('echo a"hi\'bye"boo"a\'foo"\'bb"bb\'b', "ahi'byebooa'foobb\"bbb"),
            ("echo '`echo foo`'", "`echo foo`"),
            ("echo hello`echo foo space bar`hello", "hellofoo space barhello"),
            (
                'echo hello`echo "foo space bar"`hello',
                "hellofoo space barhello",
            ),
            (
                'echo hello`echo "foo    space bar"`hello',
                "hellofoo space barhello",
            ),
            (
                'echo "hey"`echo he`"bam"`echo wow lol try`"too"',
                "heyhebamwow lol trytoo",
            ),
            (
                "echo `echo foo ; echo bar ; echo see ; echo bye`",
                "foo bar see bye",
            ),
            ('ec`echo "ho"` "foo `echo bar`"', "foo bar"),
            ("echo `echo `echo hi``", "echo hi"),
        ]
    )
    def test_quotation_cases(self, commandline, expected):
        out = parse(commandline)
        self.assertEqual("".join(out).rstrip(), expected)
