from typing import List
from application import Application


class Echo(Application):
    """
    Repeats the arguments to stdout.

    echo [ARG]...
        - ARG: Arguments to be printed to stdout. \
When no arguments are presented, stdin is used.
    """

    def execute(self, args: List[str], out: List[str]) -> None:
        """
        Executes the echo command.

        Parameters:
            args (List[str]): Arguments to be repeated by function.
            out (List[str]): Output for stdout.
        """
        out.append(" ".join(args) + "\n")
