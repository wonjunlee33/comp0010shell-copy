import fnmatch
import os
from error import ArgumentError, FlagError, DirectoryError
from os import listdir
from typing import List
from application import Application


class Find(Application):
    """
    Finds all paths where the pattern is matched.

    Usage: find [DIR]? -name [PATTERN]
        - DIR: A directory to search in. If not specified, \
uses the current directory.
        - PATTERN: The pattern to be matched.
    """

    def find(
        self, dire: str, prev: str, pattern: str, found: List[str], flag: bool
    ) -> None:
        """
        Finds paths which match the pattern.

        Parameters:
            dire (str): Current directory.
            prev (str): Previous output directory.
            pattern (str): Pattern to be matched.
            found (List[str]): Output array for matched paths.
            flag (bool): Flag for if it has been matched previously.
        """
        if os.path.isdir(dire):
            if flag:
                for f in listdir(dire):
                    if not f.startswith("."):
                        self.find(
                            os.path.join(dire, f),
                            os.path.join(prev, f),
                            pattern,
                            found,
                            True,
                        )
                        found.append(os.path.join(prev, f) + "\n")
            else:
                for f in listdir(dire):
                    if not f.startswith("."):
                        if fnmatch.fnmatch(f, pattern):
                            self.find(
                                os.path.join(dire, f),
                                os.path.join(prev, f),
                                pattern,
                                found,
                                True,
                            )
                            found.append(os.path.join(prev, f) + "\n")
                        else:
                            self.find(
                                os.path.join(dire, f),
                                os.path.join(prev, f),
                                pattern,
                                found,
                                False,
                            )

    def execute(self, args: List[str], out: List[str]) -> None:
        """
        Executes the find command.

        Parameters:
            args (List[str]): Arguments to be passed.
            out (List[str]): Output for stdout.

        Exceptions:
            ArgumentError: If wrong number of arguments passed.
            FlagError: If wrong flags passed.
            DirectoryError: If directory does not exist.
        """
        if len(args) == 0 or len(args) > 3:
            raise ArgumentError(
                """Wrong number of command line arguments \
                [find <dir>? -name <pattern>]"""
            )
        else:
            # Without PATH name.
            if len(args) == 2 and args[0] == "-name":
                ls_dir = os.getcwd()
                self.find(ls_dir, ".", args[1], out, False)

            # With PATH name.
            elif len(args) == 3 and args[1] == "-name":
                ls_dir = os.getcwd()
                if os.path.isdir(ls_dir + "/" + args[0]):
                    self.find(
                        os.path.join(ls_dir, args[0]),
                        os.path.join(args[0]),
                        args[2],
                        out,
                        False,
                    )
                else:
                    raise DirectoryError(f"Invalid Directory Name - {args[0]}")
            else:
                raise FlagError("Wrong Flags [find <dir>? -name <pattern>]")
