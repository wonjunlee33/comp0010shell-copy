from error import ArgumentError, FlagError
from typing import List
from application import Application


class Color(Application):
    """
    Changes the font color of the shell.

    Usage: color [COLOR]
        - COLOR: Specifies the color of text displayed: \
(Not all supported colors are displayed below)
            - [red]: changes the text to red.
            - [purple]: changes the text to purple.
            - [reset]: resets the text color.
    """

    def execute(self, args: List[str], out: List[str]) -> None:
        """
        Executes the color command.

        Parameters:
            args (List[str]): Arguments to be passed.
            out (List[str]): Output for stdout.

        Exceptions:
            ArgumentError: If wrong number of arguments passed.
            FlagError: If wrong flags passed.
        """
        colours = {
            "grey": "\033[30m",
            "red": "\033[31m",
            "lime": "\033[32m",
            "orange": "\033[33m",
            "blue": "\033[34m",
            "purple": "\033[35m",
            "light blue": "\033[36m",
            "ghostwhite": "\033[37m",
            "light grey": "\033[90m",
            "light red": "\033[91m",
            "light lime": "\033[92m",
            "yellow": "\033[93m",
            "light purple": "\033[95m",
            "cyan": "\033[36m",
            "white": "\033[37m",
            "reset": "\033[0m",
        }

        if 0 < len(args) <= 2:
            if " ".join(args).lower() in colours:
                out.append(colours[" ".join(args).lower()])
            else:
                raise FlagError(f"Invalid colour - {''.join(args)}")
        else:
            raise ArgumentError(
                "Wrong number of command line arguments [color <colour>]"
            )
