"""
Module to manipulate system commands
"""

from os import environ, path
from subprocess import CalledProcessError
from subprocess import run as process_run


def run(cmd_args: list[str], msg: str = ""):
    """
    The function which runs the command with error processing abilities

    Params:
        list[str] cmd_args: the command list arguments
        str msg: the message printed when an error occurred, usually started with a "when"
    """
    try:
        process_run(args=cmd_args, check=True)
    except CalledProcessError as err:
        print(
            "\033[91m\033[1m[Error]",
            "An error occurred!" if msg == "" else f"An error occurred {msg}",
        )
        print(f"\033[31mError message\033[0m\n\t{str(err)}")


def check_cmd_exists(cmd: str) -> bool:
    """
    Check if a command exists in environment PATH

    Params:
        str cmd: the command to be checked
    """
    bool_value: int = 0

    for path_item in environ["PATH"].split(":"):
        bool_value += int(path.exists(f"{path_item}/{cmd}"))
    return bool(bool_value)
