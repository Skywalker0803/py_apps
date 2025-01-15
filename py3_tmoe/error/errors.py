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


class DistroXOnlyError(Exception):
    """
    This is the error for unsupported distros

    Params:
        str unsupported_distro: the current distro that's not supported
        str supported_distro: the supported distro for this feature
    """

    def __init__(self, unsupported_distro: str, supported_distro: str) -> None:
        super().__init__()
        self.unsupported = unsupported_distro
        self.supported = supported_distro

    def __str__(self) -> str:
        msg: str = (
            "Sorry, the software / feature currently doesn't support your distro: "
            + f"{self.unsupported}"
            + "\n"
            + f"Only {self.supported} is now supported"
        )
        return universal_msg + msg


class CmdNotFoundError(Exception):
    """
    This is the error for unfound commands

    Params:
        str cmd: the command that's not found
    """

    def __init__(self, cmd: str) -> None:
        super().__init__()
        self.cmd = cmd

    def __str__(self) -> str:
        msg: str = (
            f'Sorry, the command "{self.cmd}" is not found ' + "in the system path"
        )
        return universal_msg + msg
