import os
from typing import List
from application import Application


class Pwd(Application):
    """
    Outputs the current working directory.

    Usage: pwd
    """

    def execute(self, args: List[str], out: List[str]) -> None:
        """
        Executes the pwd command.

        Parameters:
            args (List[str]): Arguments to be passed.
            out (List[str]): Output for stdout.
        """
        out.append(os.getcwd() + "\n")
