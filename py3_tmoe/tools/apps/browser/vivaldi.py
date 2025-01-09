"""
This module contains the class for managing Vivaldi browser
"""

from re import match

from bs4 import BeautifulSoup
from requests import get

from py3_tmoe.tools.utils.errors import UnsupportedArchitectureError

from py3_tmoe.tools.utils.utils import check_architecture, get_distro_short_name


class Vivaldi:
    """
    This class for managing Vivaldi browser
    """

    REPO_URL: str = "https://vivaldi.com/zh-hans/download/"

    def __init__(self) -> None:
        self.arch_type: str = check_architecture()
        self.distro, self.other_distro = get_distro_short_name()
        self.pkg_url: str = ""

    def prepare(self) -> None:
        """
        Prepare for vivaldi installation
        """

        repo_page = BeautifulSoup(get(self.REPO_URL, timeout=5).text, "html.parser")

        links: list[str] = repo_page.find_all("a")

        for link in links:
            arch_is_supported_deb: bool = self.arch_type in [
                "amd64",
                "arm64",
                "i386",
                "armhf",
            ]

            if link and arch_is_supported_deb:
                if self.distro == "debian" and match(r"*.deb", link):
                    self.pkg_url = link.replace("amd64.deb", f"{self.arch_type}.deb")

                elif (
                    self.distro == "redhat"
                    and match(r"*.rpm", link)
                    and match(r"*x86_64*", link)
                ):
                    if self.arch_type in ["amd64", "i386"]:
                        self.pkg_url = (
                            link.replace("x86_64", self.arch_type)
                            if self.arch_type == "i386"
                            else link
                        )
                        break
                    else:
                        raise UnsupportedArchitectureError(self.arch_type)

        if self.pkg_url == "":
            raise UnsupportedArchitectureError(self.arch_type)

    def install(self) -> None:
        """Install vivaldi browser"""
