"""
This module contains download functions for this proj
"""

from json import loads
from sys import exit as sys_exit

from requests import get as req_get
from requests.exceptions import RequestException

from py_apps.errors.cmd_not_found import CmdNotFoundError
from py_apps.utils.cmd import check_cmd_exists, run

import asyncio
from pyppeteer import launch
from bs4 import BeautifulSoup


def fetch_webpage_content(url, selector=None, timeout=10):  # 添加超时参数
    """
    同步抓取网页内容。

    Args:
        url (str): 网页 URL。
        selector (str, optional): 用于等待页面加载的 CSS 选择器。默认为 None。
        timeout (int, optional): 等待页面加载的超时时间（秒）。默认为 10 秒。

    Returns:
        BeautifulSoup 对象或 None 如果发生错误。
    """

    async def _fetch_content():
        try:
            browser = await launch()
            page = await browser.newPage()
            await page.goto(url, timeout=timeout * 1000)  # timeout 单位为毫秒

            if selector:
                await page.waitForSelector(selector, timeout=timeout * 1000)

            html = await page.content()
            await browser.close()
            return BeautifulSoup(html, "html.parser")
        except Exception as e:
            print(f"抓取网页出错: {e}")
            return None

    return asyncio.run(_fetch_content())  # 使用 asyncio.run() 使async函数同步执行


if __name__ == "__main__":
    url = "https://www.jetbrains.com/pycharm/download/"  # 替换成你的目标网址
    selector = ".some_element_on_the_page"  # 替换成页面上的一个 CSS 选择器，用于判断页面是否加载完成。如果不需要等待，可以设置为None
    soup = fetch_webpage_content(url, selector)

    if soup:
        # 在这里使用 BeautifulSoup 解析网页内容
        # 例如：
        # links = soup.find_all('a', {'class': 'linux-download-link'})
        # for link in links:
        #     print(link.get('href'))
        print("网页抓取成功！")
        # print(soup) # 打印BeautifulSoup 对象，方便调试
    else:
        print("网页抓取失败。")

    url_no_wait = (
        "https://www.jetbrains.com/pycharm/download/"  # 替换成你的目标网址，无需等待
    )
    soup_no_wait = fetch_webpage_content(url_no_wait)  # 不等待页面元素

    if soup_no_wait:
        print("无需等待元素，网页抓取成功！")
        # print(soup_no_wait) # 打印BeautifulSoup 对象，方便调试
    else:
        print("网页抓取失败。")


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


def get_github_releases(repo: str, version: str = "latest") -> list[str]:
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

    # Debug msg:
    # print(dumps(json_content))

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
        res.raise_for_status()
    except RequestException as err:
        print(str(err))
        sys_exit("request_error")

    return res
