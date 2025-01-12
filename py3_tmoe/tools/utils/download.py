"""
This module contains download functions for this proj
"""

from py3_tmoe.tools.utils.errors import CmdNotFoundError
from py3_tmoe.tools.utils.utils import check_cmd_exists, run


def download(
    url: str,
    file_path: str = "",
    no_conf: bool = False,
    overwrite: bool = False,
    log_level: str = "info",
    check_cert: bool = False,
    chunk: str = "1M",
    multi_thread: int = 5,
) -> None:
    """
    Thus function is for downloading files from remote url using aria2c

    Params:
        str url: the remote file url
        str file_path: the output file path
        bool no_conf: whether to use the default aria2 config file
        bool overwrite: whether to overwrite the already existed file
        str log_level: the log level of aria2c
            values: "info" | "error"
        bool check_cert: check certificate
        str chunk: download chunk size, 1M by default
        int multi_thread: download thread number
    """
    if not check_cmd_exists("aria2c"):
        raise CmdNotFoundError("aria2c")

    run(
        [
            "aria2c",
            f"--console-log-level={log_level}",
            "--no-conf" if no_conf else "",
            f"-k {chunk}",
            *f"-s {multi_thread} -x {multi_thread}".split(" "),
            f"check-certificate={str(check_cert).lower()}",
            f"--allow-overwrite={str(overwrite).lower()}",
            *f"-o {file_path}".split(" "),
            url,
        ],
        f"when downloading {url} to {file_path}",
    )
