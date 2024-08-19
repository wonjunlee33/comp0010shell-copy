import os
from typing import List, Tuple
from application import Application
from error import FileError, FlagError


class Wc(Application):
    """
    Counts the number of lines, words, and characters in a file or stdin.

    Usage: wc [OPTION] [FILE]?
        - [OPTION]: The flags to be passed. If not specified, \
returns all three counts.
            - [-l]: Returns the number of lines.
            - [-w]: Returns the number of words.
            - [-m]: Returns the number of characters.
        - [FILE]: The name of the file. If not specified, uses stdin.
    """

    @staticmethod
    def parse_arguments(args: List[str]) -> Tuple[List[str], List[str]]:
        """
        Parses command-line arguments into flags and file paths.

        Parameters:
            args (List[str]): Command-line arguments.

        Returns:
            Tuple[List[str], List[str]]: Lists of flags and file paths.
        """
        flags = []
        file_paths = []
        for arg in args:
            if arg.startswith("-"):
                flags.extend(arg[1:])
            else:
                file_paths.append(arg)
        return flags, file_paths

    @staticmethod
    def count(lines: List[str]) -> Tuple[int, int, int]:
        """
        Counts the number of lines, words, and characters in a list of strings.

        Parameters:
            lines (List[str]): List of strings representing lines of text.

        Returns:
            Tuple[int, int, int]: Count of lines, words, and characters.
        """
        num_lines = len(lines)
        num_words = sum(len(line.split()) for line in lines)
        num_chars = sum(len(line) for line in lines)
        return num_lines, num_words, num_chars

    @staticmethod
    def handle_flags(
        flags: List[str],
        num_lines: int,
        num_words: int,
        num_chars: int,
        out: List[str],
    ) -> None:
        """
        Handles specified flags and appends corresponding output.

        Parameters:
            flags (List[str]): List of flags to be processed.
            num_lines (int): Number of lines.
            num_words (int): Number of words.
            num_chars (int): Number of characters.
            out (List[str]): List to which the output will be appended.

        Exceptions:
            FlagError: If an invalid flag is passed.
        """
        if not flags:
            out += [f"{num_lines}\n", f"{num_words}\n", f"{num_chars}\n"]
        for flag in flags:
            if flag == "l":
                out.append(f"{num_lines}\n")
            elif flag == "w":
                out.append(f"{num_words}\n")
            elif flag == "m":
                out.append(f"{num_chars}\n")
            else:
                raise FlagError(f"Invalid flag: {flag}")

    def execute(self, args: List[str], out: List[str]) -> None:
        """
        Executes the wc command.

        Parameters:
            args (List[str]): Arguments to be passed.
            out (List[str]): Output for stdout.

        Exceptions:
            FlagError: If wrong flags passed.
        """
        flags, file_paths = self.parse_arguments(args)
        if not file_paths:
            lines = self.stdin_check()
            num_lines, num_words, num_chars = self.count(lines)
            self.handle_flags(flags, num_lines, num_words, num_chars, out)
        else:
            eol, words, chars = 0, 0, 0
            for file_path in file_paths:
                if not os.path.exists(file_path):
                    raise FileError(f"File '{file_path}' does not exist")
                with open(file_path, "r") as f:
                    lines = f.readlines()
                file_lines, file_words, file_chars = self.count(lines)
                eol += file_lines
                words += file_words
                chars += file_chars
            self.handle_flags(flags, eol, words, chars, out)
