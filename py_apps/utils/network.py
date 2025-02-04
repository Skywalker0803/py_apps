"""
This module contains download functions for this proj
"""

from json import loads
from sys import exit as sys_exit

from requests import get as req_get
from requests.exceptions import RequestException

from py_apps.errors.cmd_not_found import CmdNotFoundError
from py_apps.utils.cmd import check_cmd_exists, run


def download(
    url: str,
    file_path: str = "",
    no_conf: bool = True,
    overwrite: bool = False,
    check_cert: bool = False,
) -> None:
    """
    This function is for downloading files from remote url using aria2c

    Params:
        str url: the remote file url
        str file_path: the output file path, starts with a "/"
        bool no_conf: whether to use the default aria2 config file
        bool overwrite: whether to overwrite the already existed file
        bool check_cert: check certificate
    """
    if not check_cmd_exists("aria2c"):
        raise CmdNotFoundError("aria2c")

    # Parse the file_path as path and filename
    ls_of_file_and_path: list[str] = file_path.split("/")
    ls_of_file_and_path.pop(0)

    run(
        [
            "aria2c",
            # Set log level to "info"
            "--console-log-level=info",
            # Ignore global config file
            "--no-conf" if no_conf else "",
            # Set chunk size to 10 MiB
            *"-k 10M".split(" "),
            # Set process number to 5
            # an average between anti-scrap policy and download speed
            *"-s 5 -x 5".split(" "),
            # Disable check cert
            f"--check-certificate={str(check_cert).lower()}",
            # Allow overwrite or else it'll be like a.txt.1, a.txt.2 ...
            f"--allow-overwrite={str(overwrite).lower()}",
            # Set output file path to file_path
            "-o",
            "/".join(ls_of_file_and_path),
            *"-d /".split(" "),
            # Download URL
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
        get(
            f"https://api.github.com/repos/{repo}/releases/{version}",
        ).text
    )

    assets: list[str] = []

    # The data structure was like:
    # {
    #   ...
    #   "assets": [
    #       {
    #           ...
    #           "browser_download_url": "..."
    #       },
    #       ...
    #   ],
    # }
    for i in json_content["assets"]:
        assets.append(i["browser_download_url"])

    return assets


def get(url: str, headers: dict | None = None):
    """
    Encapsulation for requests.get with err processer
    """

    if headers is None:
        # Fix "dangerous" default value {}
        headers = {}
    try:
        res = req_get(url=url, headers=headers, timeout=10)
    except RequestException as err:
        print(str(err))
        sys_exit("request_error")

    return res
