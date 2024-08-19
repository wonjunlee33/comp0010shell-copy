from error import ArgumentError, FileError, FlagError
from typing import List
from application import Application


class Uniq(Application):
    """
    Removes non-unique adjacent lines from input.

    Usage: uniq [-i]? [FILE]?
        - [-i]: Ignores case.
        - FILE: The name of the file. If not specified, uses stdin.
    """

    @staticmethod
    def return_uniq(lines: List[str], ignore_case: bool) -> List[str]:
        """
        Returns a list with non-match adjacent lines.

        Parameters:
            lines (List[str]): Lines to be checked.
            ignore_case (List[str]): Flag for whether case is ignored.

        Returns:
            (List[str]): Returns list with non-unique adjacent lines removed.
        """
        return_text = [lines[0].strip("\n")]
        for i in range(1, len(lines)):
            lines[i] = lines[i].strip("\n")
            if ignore_case:
                if lines[i].lower() != return_text[-1].lower():
                    return_text.append(lines[i])
            else:
                if lines[i] != return_text[-1]:
                    return_text.append(lines[i])
        return [s + "\n" for s in return_text]

    def unique_file(self, file_name: str, ignore_case: bool) -> List[str]:
        """
        File handling for uniq.

        Parameters:
            file_name (str): File to be handled.
            ignore_case (bool): Flag for whether case is ignored.

        Returns:
            (List[str]): Returns list with matching adjacent lines removed.

        Exceptions:
            FileError: If file does not exist.
        """
        try:
            with open(file_name, "r") as file:
                lines = file.readlines()
        except FileNotFoundError:
            raise FileError(f"File does not exist - {file_name}")
        return self.return_uniq(lines, ignore_case)

    def unique_stdin(self, ignore_case: bool) -> List[str]:
        """
        Stdin handling for uniq.

        Parameters:
            ignore_case (bool): Flag for whether case is ignored.

        Returns:
            (List[str]): Returns list with matching adjacent lines removed.
        """
        lines = self.stdin_check()
        return self.return_uniq(lines, ignore_case)

    def execute(self, args: List[str], out: List[str]) -> None:
        """
        Executes the uniq command.

        Parameters:
            args (List[str]): Arguments to be passed.
            out (List[str]): Output for stdout.

        Exceptions:
            ArgumentError: If wrong number of arguments passed.
            FlagError: If wrong flags passed.
            FileError: If file does not exist.
        """
        if len(args) == 0:
            out.extend(self.unique_stdin(False))
        elif len(args) == 1:
            if args[0] == "-i":
                out.extend(self.unique_stdin(True))
            else:
                out.extend(self.unique_file(args[0], False))
        elif len(args) == 2:
            if args[0] == "-i":
                out.extend(self.unique_file(args[1], True))
            else:
                raise FlagError("Wrong flags [uniq -i <file>?]")
        else:
            raise ArgumentError(
                "Wrong number of command line arguments [uniq -i <file>?]"
            )
