import os
from error import ArgumentError, DirectoryError
from typing import List
from application import Application


class Cd(Application):
    """
    Changes the current working directory.

    Usage: cd [PATH]
        - PATH: A relative path to the target directory.
    """

    def execute(self, args: List[str], out: List[str]) -> None:
        """
        Executes the cd command.

        Parameters:
            args (List[str]): Arguments to be passed.
            out (List[str]): Output for stdout.

        Exceptions:
            ArgumentError: If wrong number of arguments passed.
            DirectoryError: If directory does not exist.
        """
        if len(args) == 0 or len(args) > 1:
            raise ArgumentError(
                "Wrong number of command line arguments [cd <dir>]"
            )
        try:
            os.chdir(args[0])
        except FileNotFoundError:
            raise DirectoryError(f"Directory does not exist - {args[0]}")
