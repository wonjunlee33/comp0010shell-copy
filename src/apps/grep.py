import re
from error import ArgumentError, FileError
from typing import List
from application import Application


class Grep(Application):
    """
    Matches a pattern in the files provided.

    Usage: grep [PATTERN] [FILE]...
        - PATTERN: A regular expression to be matched.
        - FILE(s): Name(s) of the file(s) to be searched. \
If not specified, uses stdin.
    """

    def execute(self, args: List[str], out: List[str]) -> None:
        """
        Executes the grep command.

        Parameters:
            args (List[str]): Arguments to be passed.
            out (List[str]): Output for stdout.

        Exceptions:
            ArgumentError: If wrong number of arguments passed.
            FileError: If file does not exist.
        """
        if len(args) < 1:
            raise ArgumentError(
                """Wrong number of command line arguments \
                [grep <pattern> <file>?]"""
            )

        elif len(args) == 1:
            pattern = args[0]
            lines = self.stdin_check()
            for line in lines:
                if re.match(pattern, line):
                    out.append(line)

        else:
            pattern = args[0]
            files = args[1:]
            for file in files:
                try:
                    with open(file) as f:
                        lines = f.readlines()
                        for line in lines:
                            try:
                                if re.match(pattern, line):
                                    if len(files) > 1:
                                        out.append(f"{file}:{line}")
                                    else:
                                        out.append(line)
                            except re.error:
                                raise ArgumentError(
                                    f"""Invalid regular
                                    expression pattern {pattern}"""
                                )
                except FileNotFoundError:
                    raise FileError(f"File does not exist - {file}")
            if len(out) > 0 and out[-1][-1] != "\n":
                out[-1] += "\n"
