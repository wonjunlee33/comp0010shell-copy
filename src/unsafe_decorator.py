from application import Application
from typing import List


class UnsafeDecorator(Application):
    """
    Decorator for adding exception handling to applications.

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
        Wraps the application in a try except block

        Parameters:
            args (List[str]): Arguments to be passed
            out (List[str]): Output for stdout
        """
        try:
            # Execute the wrapped command
            self.wrapped_application.execute(args, out)
        except Exception as e:
            # Catch any exceptions and print them to out
            out.append(f"An exception occurred: {str(e)}\n")
