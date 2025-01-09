"""
This module defines errors (exceptions) for the project
"""

universal_msg: str = "\033[91m\033[1m[Error]\033[0m"


class UnknownPkgManagerError(Exception):
    """
    This is the error for unknown package managers

    Params:
        str distro: the distro with pkg manager unknown
    """

    def __init__(self, distro: str) -> None:
        super().__init__()
        self.distro = distro

    def __str__(self) -> str:
        """
        This method defines the err msg of UnknownPkgManagerError

        Returns: str
        """
        msg: str = f" Unknown package manager for Linux distro: {self.distro}"
        return universal_msg + msg


class NoURLError(Exception):
    """
    This is the error for not found urls in a page

    Params:
        str page: the page which has no url found
    """

    def __init__(self, page: str) -> None:
        super().__init__()
        self.page = page

    def __str__(self) -> str:
        """
        This method defines the err msg of NoURLError

        Returns: str
        """
        msg: str = f"There aren't any links found in \033[4m\03395m{self.page}\033[0m"

        return universal_msg + msg


class UnsupportedArchitectureError(Exception):
    """
    This is the error for unsupported architectures

    Params:
        str unsupported_arch: the unsupported arch for certain feature(s)
    """

    def __init__(self, unsupported_arch: str) -> None:
        super().__init__()
        self.arch = unsupported_arch

    def __str__(self) -> str:
        msg: str = (
            "The software / feature currently doesn't support your architecture: "
            + f"{self.arch}"
        )

        return universal_msg + msg
