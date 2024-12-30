"""
This module defines errors (exceptions) for the project
"""


class UnknownPkgManagerError(Exception):
    """
    This is the error for unknown package managers
    """

    def __init__(self, distro: str) -> None:
        super().__init__()
        self.distro = distro

    def __str__(self) -> str:
        """
        This method defines the err msg of UnknownPkgManagerError

        Returns: str
        """
        msg: str = "\033[91m\033[1m[Error]\033[0m"
        msg2: str = f" Unknown package manager for Linux distro: {self.distro}"
        return msg + msg2
