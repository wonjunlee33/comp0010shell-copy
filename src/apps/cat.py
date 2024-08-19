from error import FileError
from typing import List
from application import Application


class Cat(Application):
    """
    Concatenates the content of given files and prints it to stdout.

    Usage: cat [FILE]...
        - FILE(s): Name(s) of the file(s) to concatenate. \
If no files are specified, uses stdin.
    """

    def execute(self, args: List[str], out: List[str]) -> None:
        """
        Executes the cat command.

        Parameters:
            args (List[str]): Arguments (filenames) to be passed.
            out (List[str]): Output for stdout.

        Exceptions:
            FileError: If file does not exist.
        """
        if len(args) == 0:
            out.extend(self.stdin_check())
        else:
            for a in args:
                try:
                    with open(a.rstrip()) as f:
                        # out.append(f.read())
                        out.extend(f.readlines())
                except FileNotFoundError:
                    raise FileError(f"File does not exist - {a}")
        if len(out) > 0 and out[-1][-1] != "\n":
            out[-1] += "\n"
