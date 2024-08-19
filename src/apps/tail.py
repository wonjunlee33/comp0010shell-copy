from error import ArgumentError, FileError, FlagError
from typing import List
from application import Application


class Tail(Application):
    """
    Outputs the last n lines of a file.

    Usage: tail [-n <num_lines>]? [FILE]?
        - [-n <num_lines>]: The number of lines to be returned. \
If not specified, returns the last 10 lines.
        - FILE: The name of the file. If not specified, uses stdin.
    """

    def execute(self, args: List[str], out: List[str]) -> None:
        """
        Executes the tail command.

        Parameters:
            args (List[str]): Arguments to be passed.
            out (List[str]): Output for stdout.

        Exceptions:
            ArgumentError: If wrong number of arguments passed.
            FlagError: If wrong flags passed.
            FileError: If file does not exist.
        """

        file = None

        if len(args) == 0:
            num_lines = 10

        elif len(args) == 1:
            num_lines = 10
            file = args[0]

        elif len(args) == 2:
            if args[0] != "-n":
                raise FlagError("Wrong flags [tail (-n <num_lines>)? <file>?]")
            else:
                num_lines = int(args[1])

        elif len(args) == 3:
            if args[0] != "-n":
                raise FlagError("Wrong flags [tail (-n <num_lines>)? <file>]")
            else:
                num_lines = int(args[1])
                file = args[2]
        else:
            raise ArgumentError(
                """Wrong number of command line arguments \
                [tail (-n <num_lines>)? <file>?]"""
            )

        if file:
            try:
                with open(file) as f:
                    lines = f.readlines()
            except FileNotFoundError:
                raise FileError(f"File does not exist - {file}")
        else:
            lines = self.stdin_check()

        display_length = min(len(lines), num_lines)
        for i in range(0, display_length):
            out.append(lines[len(lines) - display_length + i])
