import os
from error import ArgumentError, FlagError, DirectoryError
from typing import List
from application import Application


class Rmdir(Application):
    """
    Removes a directory and its contents.

    Usage: rmdir [DIR]
        - DIR: The path of the directory to remove.
    """

    @staticmethod
    def is_directory_empty(path: str) -> bool:
        """
        Check if a directory is empty.

        Parameters:
            path (str): Path of the directory to check.

        Returns:
            (bool): True if the directory is empty, False otherwise.
        """
        return not os.listdir(path)

    @staticmethod
    def recursive_remove(path: str) -> None:
        """
        Recursively remove all files and directories within a directory.

        Parameters:
            path (str): Path of the directory to remove.
        """
        for root, dirs, files in os.walk(path, topdown=False):
            for file in files:
                file_path = os.path.join(root, file)
                os.remove(file_path)
            for dir_name in dirs:
                dir_path = os.path.join(root, dir_name)
                os.rmdir(dir_path)

    def execute(self, args: List[str], out: List[str]) -> None:
        """
        Executes the rmdir command.

        Parameters:
            args (List[str]): Arguments to be passed.
            out (List[str]): Output for stdout.

        Exceptions:
            ArgumentError: If wrong number of arguments passed.
            DirectoryError: If directory does not exist.
            FlagError: If wrong flags are passed.
        """
        if len(args) != 1 and len(args) != 2:
            raise ArgumentError("Wrong number of command line arguments")
        if len(args) == 1:
            directory_path = args[0]
            if not os.path.exists(directory_path):
                raise DirectoryError(
                    f"Directory does not exist - {directory_path}"
                )
            if self.is_directory_empty(directory_path):
                os.rmdir(directory_path)
            else:
                raise DirectoryError(
                    f"Directory is not empty - {directory_path}"
                )
        else:
            flag, directory_path = args
            if flag not in ["-r", "-rf"]:
                raise FlagError("Wrong flags")
            if not os.path.exists(directory_path):
                raise DirectoryError(
                    f"Directory does not exist - {directory_path}"
                )
            self.recursive_remove(directory_path)
            os.rmdir(directory_path)
