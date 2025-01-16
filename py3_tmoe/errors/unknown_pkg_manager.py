"""UnknownPkgManagerError"""

from .common import universal_msg


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
