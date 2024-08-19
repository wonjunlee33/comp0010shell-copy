import io
import os
import sys
import readline
from antlr.Comp0010ShellLexer import Comp0010ShellLexer
from antlr.Comp0010ShellParser import Comp0010ShellParser
from antlr4 import InputStream, CommonTokenStream
from error import (
    ArgumentError,
    FlagError,
    FileError,
    RedirectError,
    ApplicationError,
    DirectoryError,
)
from typing import List
from visitor import Visitor


def parse(cmdline: str) -> List[str]:
    """
    Parses a command line input and returns the execution result.

    Parameters:
        cmdline (str): Command line input.

    Returns:
        List[str]: Output deque.
    """
    input_stream = InputStream(io.StringIO(cmdline).read())
    lexer = Comp0010ShellLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = Comp0010ShellParser(stream)
    tree = parser.command()
    visitor = Visitor()
    visitor.visit(tree)
    return [item for sublist in visitor.output for item in sublist]


def catch_error(cmdline: str) -> None:  # pragma: no cover
    """
    Catches errors for interactive mode.

    Parameters:
        cmdline (str): Command line input.
    """
    try:
        out = parse(cmdline)
        for result in out:
            print(result, end="")
    except (
        ValueError,
        ArgumentError,
        ApplicationError,
        DirectoryError,
        FileError,
        FlagError,
        RedirectError,
    ) as e:
        print(
            f"The following error has occurred: [{e.__class__.__name__}] {e}"
        )


def interactive_mode() -> None:  # pragma: no cover
    """
    Enters the interactive mode.
    """
    print("Welcome to the Comp0010 Shell! 🐚")
    while True:
        try:
            cmdline = input(os.getcwd() + "> ")
            readline.set_auto_history(True)
            readline.parse_and_bind("tab: complete")
            catch_error(cmdline)
        except KeyboardInterrupt:
            print("\nExiting shell. Goodbye! 👋")
            break


def run() -> None:  # pragma: no cover
    """
    Runs the shell.
    """
    args_num = len(sys.argv) - 1
    if args_num > 0:
        if args_num != 2:
            raise ValueError("Wrong number of command line arguments")
        if sys.argv[1] != "-c":
            raise ValueError(f"Unexpected command line argument {sys.argv[1]}")
        out = parse(sys.argv[2])
        for result in out:
            print(result, end="")
    else:
        interactive_mode()


if __name__ == "__main__":  # pragma: no cover
    run()
