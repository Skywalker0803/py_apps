"""
Other utils in this proj
"""

from os import path
from re import sub
from subprocess import check_output

from py_apps.utils.app_manage import install_app

import asyncio
from pyppeteer import launch
from bs4 import BeautifulSoup


def fetch_webpage_content(url, selector=None, timeout=10):  # 添加超时参数
    """
    同步抓取网页内容。

    Args:
        str url: Webpage URL
        str? selector: CSS selector waiting to be loaded, None by default
        int? timeout: timeout waiting for load, 10s by default

    Returns: BeautifulSoup object
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

    # print("网页抓取失败。")


def to_snakecase(string: str):
    """
    Params:
        str string: the input string
    """

    return "_".join(
        sub(
            "([A-Z][a-z]+)", r" \1", sub("([A-Z]+)", r" \1", string.replace("-", " "))
        ).split()
    ).lower()


def fix_electron_libxssl(distro: str) -> None:
    """Fix electron libxssl problem"""
    match distro:
        case "debian":
            if not check_output(["whereis", "libnss3.so"]) == "libnss3.so:":
                install_app(distro, ["libnss3"])
        case "redhat":
            install_app(distro, ["libXScrnSaver"])
        case "arch":
            if not path.exists("/usr/lib/libnss3.so"):
                install_app(distro, ["nss"])
        case "suse":
            install_app(distro, ["mozilla-nss"])
        case _:
            install_app(distro, ["nss"])
