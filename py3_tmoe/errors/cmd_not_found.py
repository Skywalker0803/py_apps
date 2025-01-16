"""CmdNotFoundError"""

from .common import universal_msg


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
