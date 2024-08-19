from error import ArgumentError, FlagError
from typing import List
from application import Application


class Font(Application):
    """
    Changes the current font.

    Usage: font [FONT]
        - FONT: Specifies the style of the text displayed to one of \
the following:
            - bold, italic, underline, crossed, dark, reversed, reset.
    """

    def execute(self, args: List[str], out: List[str]) -> None:
        """
        Changes the curent font.

        Parameters:
            args (List[str]): Arguments to be passed.
            out (List[str]): Output for stdout.

        Exceptions:
            ArgumentError: If wrong number of arguments passed.
            FlagError: If wrong flags passed.
        """
        fonts = {
            "bold": "\033[1m",
            "dark": "\033[2m",
            "italic": "\033[3m",
            "underline": "\033[4m",
            "reversed": "\033[7m",
            "crossed": "\033[9m",
            "reset": "\033[0m",
        }

        if len(args) == 1:
            if args[0].lower() in fonts:
                out.append(fonts[args[0].lower()])
            else:
                raise FlagError(f"Invalid font option - {args[0]}")
        else:
            raise ArgumentError(
                "Wrong number of command line arguments [font <font>]"
            )
