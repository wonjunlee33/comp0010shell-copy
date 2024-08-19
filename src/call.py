from application_factory import ApplicationFactory
import sys
from error import RedirectError, ApplicationError
from typing import List, IO


class Call:
    """
    Class to handle the execution of applications.

    Methods:
        eval (List[str], List[str]): Evaluates the given commands.
        redirect (str, List[str], List[str], List[str], IO): \
Performs input/output redirection.
    """

    def __init__(
        self,
        app: str,
        inputIO: List[str],
        outputIO: List[str],
        output: List[str],
        pipe: IO = None,
    ) -> None:
        self.redirect(app, inputIO, outputIO, output, pipe)

    def eval(self, commands: List[str], out: List[str]) -> None:
        """
        Evaluate the given commands and execute the corresponding application.

        Parameters:
            commands (List[str]): List of commands.
            out (List[str]): List to which the output will be appended.
        """
        application_factory = ApplicationFactory()
        app = commands[0]
        args = commands[1:]

        if app in application_factory.application_map:
            application_factory.application_map[app].execute(args, out)
        else:
            raise ApplicationError(f"Unsupported application {app}")

    def redirect(
        self,
        app: str,
        inputIO: List[str],
        outputIO: List[str],
        output: List[str],
        pipe: IO = None,
    ) -> None:
        """
        Perform input/output redirection for the specified application.

        Parameters:
            app (str): Application name.
            inputIO (List[str]): List of input file paths.
            outputIO (List[str]): List of output file paths.
            output (List[str]): List containing the final output.
            pipe (StringIO): Pipe object for input redirection.

        Exceptions:
            RedirectError: If there are invalid redirections.
        """
        if len(inputIO) > 1 or len(outputIO) > 1:
            raise RedirectError("Too many redirections")

        saved_stdin, saved_stdout = sys.stdin, sys.stdout
        input_stream, output_file = None, None

        if inputIO and pipe:
            raise RedirectError(
                "Cannot redirect input and pipe at the same time"
            )
        elif pipe:
            sys.stdin = pipe
        elif inputIO:
            try:
                input_stream = open(inputIO.pop(), "r")
            except FileNotFoundError:
                raise RedirectError("Input file not found")
            sys.stdin = input_stream

        self.eval(app, output[-1])

        if outputIO:
            output_name, setting = outputIO.pop()
            output_file = open(output_name, setting)
            output_file.write("".join(output.pop()))

        if input_stream:
            input_stream.close()
        if output_file:
            output_file.close()

        sys.stdin, sys.stdout = saved_stdin, saved_stdout
