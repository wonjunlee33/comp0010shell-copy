from application import Application
from typing import List


class HelpDecorator(Application):
    """
    Decorator for adding help functionality to applications.

    Attributes:
        wrapped_application (Application): Application to be decorated.

    Methods:
        execute (List[str], List[str]): Executes the application.

    Implements:
        Application: Interface for all applications.
    """

    def __init__(self, wrapped_application: Application) -> None:
        self.wrapped_application = wrapped_application

    def execute(self, args: List[str], out: List[str]) -> None:
        """
        Adds the -h and --help flags to the wrapped application.

        Parameters:
            args (List[str]): Arguments to be passed.
            out (List[str]): Output for stdout.
        """
        if args and (args[0] == "-h" or args[0] == "--help"):
            out.append(self.wrapped_application.__doc__ + "\n")
        else:
            self.wrapped_application.execute(args, out)
