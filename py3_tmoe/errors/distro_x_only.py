"""
DistroXOnlyError, for distros that aren't supported for this feature
"""

from .common import universal_msg


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
