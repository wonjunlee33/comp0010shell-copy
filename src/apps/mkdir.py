import os
from error import ArgumentError, DirectoryError
from typing import List
from application import Application


class Mkdir(Application):
    """
    Creates a directory.

    Usage: mkdir [DIR]
        - DIR: The name of the directory to create.
    """

    def execute(self, args: List[str], out: List[str]) -> None:
        """
        Executes the mkdir command.

        Parameters:
            args (List[str]): Arguments to be passed.
            out (List[str]): Output for stdout.

        Exceptions:
            ArgumentError: If wrong number of arguments passed.
            DirectoryError: If directory already exists.
        """
        if len(args) != 1:
            raise ArgumentError("Wrong number of command line arguments")
        else:
            try:
                os.mkdir(args[0])
            except FileExistsError:
                raise DirectoryError("Directory already exists")
