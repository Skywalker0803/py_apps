"""
This module contains download functions for this proj
"""

from py3_tmoe.error.errors import CmdNotFoundError
from py3_tmoe.utils.utils import check_cmd_exists, run


def download(
    url: str,
    file_path: str = "",
    no_conf: bool = False,
    overwrite: bool = False,
    check_cert: bool = False,
) -> None:
    """
    Thus function is for downloading files from remote url using aria2c

    Params:
        str url: the remote file url
        str file_path: the output file path
        bool no_conf: whether to use the default aria2 config file
        bool overwrite: whether to overwrite the already existed file
        bool check_cert: check certificate
    """
    if not check_cmd_exists("aria2c"):
        raise CmdNotFoundError("aria2c")

    run(
        [
            "aria2c",
            "--console-log-level=info",
            "--no-conf" if no_conf else "",
            "-k 1M",
            *"-s 5 -x 5".split(" "),
            f"check-certificate={str(check_cert).lower()}",
            f"--allow-overwrite={str(overwrite).lower()}",
            *f"-o {file_path}".split(" "),
            url,
        ],
        f"when downloading {url} to {file_path}",
    )
