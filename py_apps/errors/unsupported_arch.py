"""
UnsupportedArchitectureError
"""

from .common import universal_msg


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
