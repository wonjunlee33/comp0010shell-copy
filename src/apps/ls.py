import os
from error import ArgumentError, DirectoryError
from os import listdir
from typing import List
from application import Application


class Ls(Application):
    """
    Lists files in current directory.

    Usage: ls [DIR]?
        - DIR: The directory to list. If not specified, \
uses the current directory.
    """

    def execute(self, args: List[str], out: List[str]) -> None:
        """
        Executes the ls command.

        Parameters:
            args (List[str]): Arguments to be passed.
            out (List[str]): Output for stdout.

        Exceptions:
            ArgumentError: If wrong number of arguments passed.
            DirectoryError: If directory does not exist.
        """
        if len(args) == 0:
            ls_dir = os.getcwd()
        elif len(args) > 1:
            raise ArgumentError(
                "Wrong number of command line arguments [ls <dir>?]"
            )
        else:
            ls_dir = args[0]

        try:
            for f in listdir(ls_dir):
                if not f.startswith("."):
                    out.append(f + "\n")
        except FileNotFoundError:
            raise DirectoryError(f"Directory does not exist - {ls_dir}")
