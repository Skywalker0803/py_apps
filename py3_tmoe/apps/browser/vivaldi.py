"""
This module contains the class for managing Vivaldi browser
"""

from re import search

from bs4 import BeautifulSoup
from requests import get

from py3_tmoe.apps.browser.common import Browser
from py3_tmoe.errors.distro_x_only import DistroXOnlyError
from py3_tmoe.errors.unsupported_arch import UnsupportedArchitectureError
from py3_tmoe.utils.app_manage import install_app
from py3_tmoe.utils.cmd import run
from py3_tmoe.utils.network import download
from py3_tmoe.utils.sys import check_architecture, get_distro_short_name


class Vivaldi(Browser):
    """
    This class for managing Vivaldi browser
    """

    REPO_URL: str = "https://vivaldi.com/zh-hans/download/"

    _DISTRO, _OTHER_DISTRO = get_distro_short_name()
    _ARCH_TYPE: str = check_architecture()

    def __init__(self) -> None:
        self.pkg_url: str = ""
        self.use_sys_pkg_manager: bool = True if self._DISTRO == "gentoo" else False

    def prepare(self) -> Browser:
        """
        Prepare for vivaldi installation

        Throws: DistroXOnlyError
        """

        # Raise DistroXOnlyError if distro isn't debian or redhat
        if (
            self._DISTRO not in ["debian", "redhat"]
            and self.use_sys_pkg_manager is False
        ):
            raise DistroXOnlyError(self._DISTRO, "debian & redhat")

        # Use BeautifulSoup to parse the vivaldi download page for getting the download link
        repo_page = BeautifulSoup(get(self.REPO_URL, timeout=None).text, "html.parser")

        # Find all links in download page
        links = repo_page.find_all("a")

        # Iterate the links to find the correct pkg link
        for link_element in links:
            link = link_element["href"]

            # Supported architecture for deb pkgs
            arch_is_supported_deb: bool = self._ARCH_TYPE in [
                "amd64",
                "arm64",
                "i386",
                "armhf",
            ]

            # If the link isn't null
            if link and arch_is_supported_deb:
                # If the link exists and is a deb link
                if self._DISTRO == "debian" and search(r".[.]deb", link):
                    self.pkg_url = link.replace("amd64.deb", f"{self._ARCH_TYPE}.deb")

                elif (
                    self._DISTRO == "redhat"
                    and search(r".[.]rpm", link)
                    and search(r".x86_64.", link)
                ):
                    if self._ARCH_TYPE in ["amd64", "i386"]:
                        self.pkg_url = (
                            # Change the link's architecture to i386 to match the architecture
                            # The "amd64" is "x86_64" for rpms
                            link.replace("x86_64", self._ARCH_TYPE)
                            if self._ARCH_TYPE == "i386"
                            else link
                        )
                        break

                elif self._DISTRO == "gentoo":
                    self.pkg_url = "www-client/vivaldi-snapshot"

        # Raise an error if there's no found url matches the conditions
        if self.pkg_url == "":
            raise UnsupportedArchitectureError(self._ARCH_TYPE)

        return self

    def install(self) -> Browser:
        """
        Install vivaldi browser
        """

        # Let the file path be /tmp/vivaldi.{Package name extension by distro}
        file_path: str = f"/tmp/vivaldi.{self.pkg_url[-3:-1]+self.pkg_url[-1]}"

        # Download the package from website except
        # when use_sys_pkg_manager is True
        (
            download(url=self.pkg_url, file_path=file_path, overwrite=True)
            if self.use_sys_pkg_manager is False
            else None
        )

        # For deb based distros
        if self._DISTRO == "debian":
            run(
                cmd_args=["sudo", "apt", "install", "-y", file_path],
                msg="when trying to install vivaldi browser in /tmp",
            )

        # For rhel based distros
        elif self._DISTRO == "redhat":
            run(
                cmd_args=["sudo", "rpm", "-ivh", file_path],
                msg="when trying to install vivaldi browser in /tmp",
            )

        # If distro is based on gentoo, install pkg from repo
        elif self._DISTRO == "gentoo":
            install_app(self._DISTRO, [self.pkg_url])

        # Add "--no-sandbox" to application launcher
        run(
            cmd_args=[
                "sed",
                "-i",
                "s@Exec=/usr/bin/vivaldi-stable@& --no-sandbox@g",
                "/usr/share/applications/vivaldi-stable.desktop",
            ],
            msg="when adding no-sandbox to vivaldi",
        )

        return self
