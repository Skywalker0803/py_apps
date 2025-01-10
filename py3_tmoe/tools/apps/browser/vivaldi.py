"""
This module contains the class for managing Vivaldi browser
"""

from re import match

from bs4 import BeautifulSoup
from requests import get

from ...utils.errors import DistroXOnlyError, UnsupportedArchitectureError
from ...utils.utils import check_architecture, get_distro_short_name


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

        Throws: DistroXOnlyError
        """

        # Raise DistroXOnlyError if distro isn't debian or redhat
        if self.distro not in ["debian", "redhat"]:
            raise DistroXOnlyError(self.distro, "debian & redhat")

        # Use BeautifulSoup to parse the vivaldi download page for getting the download link
        repo_page = BeautifulSoup(get(self.REPO_URL, timeout=5).text, "html.parser")

        # Find all links in download page
        links: list[str] = repo_page.find_all("a")

        # Iterate the links to find the correct pkg link
        for link in links:
            # Supported architecture for deb pkgs
            arch_is_supported_deb: bool = self.arch_type in [
                "amd64",
                "arm64",
                "i386",
                "armhf",
            ]

            # If the link isn't null
            if link and arch_is_supported_deb:
                # If the link exists and is a deb link
                if self.distro == "debian" and match(r"*.deb", link):
                    self.pkg_url = link.replace("amd64.deb", f"{self.arch_type}.deb")

                elif (
                    self.distro == "redhat"
                    and match(r"*.rpm", link)
                    and match(r"*x86_64*", link)
                ):
                    if self.arch_type in ["amd64", "i386"]:
                        self.pkg_url = (
                            # Change the link's architecture to i386 to match the architecture
                            # The "amd64" is "x86_64" for rpms
                            link.replace("x86_64", self.arch_type)
                            if self.arch_type == "i386"
                            else link
                        )
                        break
                    else:
                        # Raise an error if there's no found url matches the conditions
                        raise UnsupportedArchitectureError(self.arch_type)

        # Raise an error if there's no found url matches the conditions
        if self.pkg_url == "":
            raise UnsupportedArchitectureError(self.arch_type)

    def install(self) -> None:
        """Install vivaldi browser"""
