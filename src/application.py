import sys
from error import ArgumentError, ApplicationError
from typing import List


class Application:
    """
    Interface for all applications.

    Methods:
        execute (List[str], List[str]): Executes the application.
        stdin_check (): Checks for stdin.

    Exceptions:
        ApplicationError: If parent class execute method is called.
    """

    def execute(self, args: List[str], out: List[str]) -> None:
        raise ApplicationError("Calling parent class execute method")

    @staticmethod
    def stdin_check() -> List[str]:
        """
        Stdin handling with exception.

        Returns:
            (List[str]): Returns list of lines read from stdin.

        Exceptions:
            ArgumentError: If no standard input detected.
        """
        lines = sys.stdin.readlines()
        if lines:
            return lines
        else:
            raise ArgumentError("No standard input detected")
