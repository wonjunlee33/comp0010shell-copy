import sys
from application import Application
from typing import List


class Exit(Application):
    """
    Exits the shell.

    Usage: exit
    """

    def execute(self, args: List[str] = None, out: List[str] = None) -> None:
        """
        Executes the exit command.

        Parameters:
            args (List[str]): Arguments to be passed.
            out (List[str]): Output for stdout.
        """
        print("Exiting shell. Goodbye! 👋")
        sys.exit()
