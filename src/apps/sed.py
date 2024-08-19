import os
import re
from error import ArgumentError, FileError
from typing import List
from application import Application


class Sed(Application):
    """
    Replaces a string with another string in a file.

    Usage: sed [ARG] [FILE]
        - ARG: s/pattern/replacement_string/[g]?
            - [s]: Substitute.
            - [pattern]: Regular expression pattern to be matched.
            - [replacement_string]: String to be replaced with.
            - [g]: Global flag to replace all occurrences.
        - FILE: File to be modified.
    """

    def execute(self, args: List[str], out: List[str]) -> None:
        """
        Executes the sed command.

        Parameters:
            args (List[str]): Arguments to be passed.
            out (List[str]): Output for stdout.

        Exceptions:
            ArgumentError: If invalid (regex) or wrong \
number of arguments passed.
        """
        if len(args) > 2 or len(args) == 0:
            raise ArgumentError("Wrong number of command line arguments")
        if len(args) == 1:
            # read from stdin
            try:
                process, pattern, replacement_string, flags = re.split(
                    r"[/|]", args[0]
                )
            except Exception:
                raise ArgumentError(
                    f"""Invalid regular expression pattern {args[0]}"""
                )
            lines = self.stdin_check()
            for line in lines:
                # handle regex substitution here
                if "g" in flags:
                    modified_line = re.sub(pattern, replacement_string, line)
                else:
                    modified_line = re.sub(
                        pattern, replacement_string, line, count=1
                    )
                out.append(modified_line)
            if out[-1][-1] != "\n":
                out[-1] += "\n"
        else:
            arg2, file_path = args
            try:
                process, pattern, replacement_string, flags = re.split(
                    r"[/|]", arg2
                )
            except Exception:
                raise ArgumentError(
                    f"""Invalid regular expression pattern {arg2}"""
                )
            if not os.path.exists(file_path):
                raise FileError(f"File '{file_path}' does not exist")
            with open(file_path, "r") as f:
                lines = f.readlines()
            with open(file_path, "w") as f:
                for line in lines:
                    if "g" in flags:
                        modified_line = re.sub(
                            pattern, replacement_string, line
                        )
                    else:
                        modified_line = re.sub(
                            pattern, replacement_string, line, count=1
                        )
                    f.write(modified_line)
                    out.append(modified_line)
                if out[-1][-1] != "\n":
                    out[-1] += "\n"
