import os
from typing import List
from application import Application
from error import ArgumentError, FlagError, DirectoryError, FileError


class Cp(Application):
    """
    Copies a file/directory from a source to a destination.

    Usage: cp [OPTION] [SOURCE] [DESTINATION]
        - OPTION: Specifies the behaviour of cp:
            - [-f]: forces a file to be overwritten.
            - [-r]: performs a recursive copy for \
directories (All subfiles and subdirectories copied).
        - SOURCE: Specifies the file/directory to be copied.
        - DESTINATION: Specifies the output file/directory.
    """

    @staticmethod
    def copy_file(
        source: str, destination: str, force: bool, recursive: bool
    ) -> None:
        """
        Checks whether desired destination exists and copies file.

        Parameters:
            source (str): Source file or pattern.
            destination (str): Destination directory.
            force (bool): force overwrite.
            recursive (bool): copy directories recursively.

        Exceptions:
            FileError: Invalid file passed.
            DirectoryError: Invalid directory passed.
        """
        if os.path.isfile(source):
            dest_file = destination
        elif os.path.isdir(source):
            if os.path.isfile(destination):
                raise DirectoryError("Cannot copy a directory into a file.")
            dest_file = (
                os.path.join(destination, os.path.basename(source))
                if os.path.isdir(destination)
                else destination
            )
        else:
            raise FileError(f"Source '{source}' does not exist.")
        if os.path.exists(dest_file):
            if not force:
                raise FileError(
                    f"""Destination file '{dest_file}' already exists. \
                    Use -f to force overwrite"""
                )
        if recursive:
            if os.path.isdir(source):
                for root, dirs, files in os.walk(source):
                    rel_root = os.path.relpath(root, source)
                    dest_root = os.path.join(destination, rel_root)
                    os.makedirs(dest_root, exist_ok=True)
                    for file in files:
                        src_path = os.path.join(root, file)
                        dest_path = os.path.join(dest_root, file)
                        with open(src_path, "r") as f:
                            source_lines = f.readlines()
                        with open(dest_path, "w") as f:
                            f.writelines(source_lines)
            else:
                raise FileError("Cannot copy a file recursively.")
        else:
            with open(source, "r") as f:
                source_lines = f.readlines()
            with open(dest_file, "w") as f:
                f.writelines(source_lines)

    def execute(self, args: List[str], out: List[str]) -> None:
        """
        Executes the cp command.

        Parameters:
            args (List[str]): Arguments to be passed.
            out (List[str]): Output for stdout.

        Exceptions:
            ArgumentError: If wrong number of arguments passed.
            FlagError: If wrong flags are passed.
        """
        if len(args) < 2 or len(args) > 3:
            raise ArgumentError(
                "Insufficient number of command line arguments"
            )
        force = False
        recursive = False
        while args[0].startswith("-"):
            option = args.pop(0)
            if option == "-f":
                force = True
            elif option == "-r" or option == "-R":
                recursive = True
            else:
                raise FlagError(f"Invalid option: {option}")

        source = args[0]
        destination = args[1]
        self.copy_file(source, destination, force, recursive)
