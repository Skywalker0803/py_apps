"""
This module contains download functions for this proj
"""

from json import loads

from requests import get

from py3_tmoe.errors.cmd_not_found import CmdNotFoundError
from py3_tmoe.utils.utils import check_cmd_exists, run


def download(
    url: str,
    file_path: str = "",
    no_conf: bool = True,
    overwrite: bool = False,
    check_cert: bool = False,
) -> None:
    """
    Thus function is for downloading files from remote url using aria2c

    Params:
        str url: the remote file url
        str file_path: the output file path, starts with a "/"
        bool no_conf: whether to use the default aria2 config file
        bool overwrite: whether to overwrite the already existed file
        bool check_cert: check certificate
    """
    if not check_cmd_exists("aria2c"):
        raise CmdNotFoundError("aria2c")

    ls_of_file_and_path: list[str] = file_path.split("/")
    ls_of_file_and_path.pop(0)

    run(
        [
            "aria2c",
            "--console-log-level=info",
            "--no-conf" if no_conf else "",
            *"-k 5M".split(" "),
            *"-s 5 -x 5".split(" "),
            f"--check-certificate={str(check_cert).lower()}",
            f"--allow-overwrite={str(overwrite).lower()}",
            "-o",
            "/".join(ls_of_file_and_path),
            *"-d /".split(" "),
            url,
        ],
        f"when downloading {url} to {file_path}",
    )


def get_github_releases(repo: str, version: str = "latest"):
    """
    Get the GitHub releases file url list

    Params:
        repo: the repo path to be parsed, in the form of "RepoOwner/RepoName"
        version: the version wanted, "latest" by default
    """
    json_content: dict = loads(
        get(f"https://api.github.com/repo/{repo}/releases/{version}").text
    )
    assets: list[str] = []

    for i in json_content["assets"]:
        assets.append(i["browser_download_url"])

    return assets
