from error import ArgumentError, FileError, FlagError
from typing import List
from application import Application


class Cut(Application):
    """
    Cuts out sections from each line of a given file \
or stdin and prints the result to stdout.

    Usage: cut [OPTION] [FILE]
        - OPTION: Specifies the bytes to extract from each line:
            - [-b 1,2,3]: extracts 1st, 2nd and 3rd bytes.
            - [-b 1-3,5-7]: extracts the bytes from 1st to 3rd \
and from 5th to 7th.
            - [-b -3,5-]: extracts the bytes from the beginning of \
line to 3rd, and from 5th to the end of line.
        - FILE: A name of a file. If not specified, uses stdin.
    """

    @staticmethod
    def define_ranges(byte_ranges: List[str]) -> List[str]:
        """
        Splits and defines the ranges for cut.

        Parameters:
            byte_ranges (List[str]): Initial input arguments.

        Returns:
            (List[str]): Returns list of ranges.
        """
        byte_ranges = byte_ranges.split(",")

        for i, j in enumerate(byte_ranges):
            byte_ranges[i] = j.split("-")
            if len(byte_ranges[i]) == 1:
                byte_ranges[i].append(byte_ranges[i][0])
            elif byte_ranges[i][0] == "":
                byte_ranges[i][0] = "1"

        byte_ranges.sort(key=lambda a: int(a[0]))

        intervals = []

        start, end = "0", "0"

        for rng in byte_ranges:
            if int(rng[0]) <= int(end) and rng[1] == "":
                intervals.append([start, ""])
                break
            elif rng[1] == "":
                intervals.append([start, end])
                start, end = rng
                break
            elif int(rng[0]) <= int(end) and int(rng[1]) > int(end):
                end = rng[1]
            elif int(rng[0]) > int(end):
                intervals.append([start, end])
                start, end = rng

        if intervals[-1][1] != "":
            intervals.append([start, end])

        return intervals[1:]

    def execute(self, args: List[str], out: List[str]) -> None:
        """
        Executes the cut command.

        Parameters:
            args (List[str]): Arguments to be passed.
            out (List[str]): Output for stdout.

        Exceptions:
            ArgumentError: If wrong number of arguments passed.
            FlagError: If wrong flags passed.
            FileError: If file does not exist.
        """
        if len(args) == 0 or len(args) > 3:
            raise ArgumentError(
                """Wrong number of command line arguments \
                [cut -b <byte_range> <file>?]"""
            )

        if args[0] != "-b":
            raise FlagError("Wrong flag [cut -b <byte_range> <file>?]")

        bytes_range = args[1]
        if len(args) == 2:
            lines = self.stdin_check()
        else:
            try:
                with open(args[2], "r") as file:
                    lines = file.readlines()
            except FileNotFoundError:
                raise FileError(f"File does not exist - {args[2]}")

        byte_ranges_interval = self.define_ranges(bytes_range)

        for line in lines:
            line_output = []
            line = line.strip()
            for byte_range in byte_ranges_interval:
                start, end = byte_range
                start = int(start) - 1 if start else None
                end = int(end) if end else None
                line_output.append(line[start:end])

            out.append("".join(line_output) + "\n")
