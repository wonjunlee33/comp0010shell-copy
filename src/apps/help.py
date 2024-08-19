from application import Application
from error import ArgumentError


class Help(Application):
    """
    Prints the help message.
    """

    def execute(self, args=None, out=None) -> None:
        """
        Executes the help command.

        Parameters:
            args (List[str]): Arguments to be passed.
            out (List[str]): Output for stdout.

        Exceptions:
            ArgumentError: If wrong number of arguments passed.
        """
        if len(args) > 0:
            raise ArgumentError(
                "Wrong number of command line arguments [help]"
            )

        out.append(
            """
    Usage 🚀:

        <command> [<args>] : Run one of the available commands.
        > <file> : Redirect output to a file.
        >> <file> : Append output to a file.
        < <file> : Use a file as input.
        <command> | <command> : Pipe output from one command to another.
        <command> ; <command> : Run multiple commands sequentially.

    The following commands are available 🤖:

        pwd, cd, echo, ls, ls, cat, head, tail, grep, sort, cut, \
find, uniq, mkdir, touch, rm, rmdir, mv, cp, color, font, sed, wc, exit

    Use <command> --help or <command> -h for more information about a command.
    """
            + "\n"
        )
