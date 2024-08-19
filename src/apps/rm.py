import os
from error import ArgumentError, FileError, DirectoryError
from typing import List
from application import Application


class Rm(Application):
    """
    Removes a file.

    Usage: rm [PATH]
        - PATH: The path to the file to remove.
    """

    def execute(self, args: List[str], out: List[str]) -> None:
        """
        Executes the rm command.

        Parameters:
            args (List[str]): Arguments to be passed.
            out (List[str]): Output for stdout.

        Exceptions:
            ArgumentError: If wrong number of arguments passed.
            DirectoryError: If directory is passed.
            FileError: If file does not exist.
        """
        if len(args) != 1:
            raise ArgumentError("Wrong number of command line arguments")
        elif os.path.isdir(args[0]):
            raise DirectoryError(f"Cannot remove a directory - {args[0]}")
        else:
            try:
                os.remove(args[0])
            except FileNotFoundError:
                raise FileError(f"File does not exist - {args[0]}")
