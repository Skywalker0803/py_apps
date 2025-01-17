"""
This module contains the class for managing Vivaldi browser
"""

from re import search

from bs4 import BeautifulSoup
from requests import get

from py3_tmoe.errors.distro_x_only import DistroXOnlyError
from py3_tmoe.errors.unsupported_arch import UnsupportedArchitectureError
from py3_tmoe.utils.download import download
from py3_tmoe.utils.utils import check_architecture, get_distro_short_name, run


class Vivaldi:
    """
    This class for managing Vivaldi browser
    """

    REPO_URL: str = "https://vivaldi.com/zh-hans/download/"

    DISTRO, OTHER_DISTRO = get_distro_short_name()
    ARCH_TYPE: str = check_architecture()

    def __init__(self) -> None:
        self.pkg_url: str = ""

    def prepare(self) -> None:
        """
        Prepare for vivaldi installation

        Throws: DistroXOnlyError
        """

        # Raise DistroXOnlyError if distro isn't debian or redhat
        if self.DISTRO not in ["debian", "redhat"]:
            raise DistroXOnlyError(self.DISTRO, "debian & redhat")

        # Use BeautifulSoup to parse the vivaldi download page for getting the download link
        repo_page = BeautifulSoup(get(self.REPO_URL, timeout=5).text, "html.parser")

        # Find all links in download page
        links = repo_page.find_all("a")

        # Iterate the links to find the correct pkg link
        for link_element in links:
            link = link_element["href"]

            # Supported architecture for deb pkgs
            arch_is_supported_deb: bool = self.ARCH_TYPE in [
                "amd64",
                "arm64",
                "i386",
                "armhf",
            ]

            # If the link isn't null
            if link and arch_is_supported_deb:
                # If the link exists and is a deb link
                if self.DISTRO == "debian" and search(r".[.]deb", link):
                    self.pkg_url = link.replace("amd64.deb", f"{self.ARCH_TYPE}.deb")

                elif (
                    self.DISTRO == "redhat"
                    and search(r".[.]rpm", link)
                    and search(r".x86_64.", link)
                ):
                    if self.ARCH_TYPE in ["amd64", "i386"]:
                        self.pkg_url = (
                            # Change the link's architecture to i386 to match the architecture
                            # The "amd64" is "x86_64" for rpms
                            link.replace("x86_64", self.ARCH_TYPE)
                            if self.ARCH_TYPE == "i386"
                            else link
                        )
                        break

        # Raise an error if there's no found url matches the conditions
        if self.pkg_url == "":
            raise UnsupportedArchitectureError(self.ARCH_TYPE)

    def install(self) -> None:
        """
        Install vivaldi browser
        """

        if self.DISTRO in ["debian", "redhat"]:

            file_path: str = f"/tmp/vivaldi.{self.pkg_url[-3:-1]+self.pkg_url[-1]}"

            download(url=self.pkg_url, file_path=file_path, overwrite=True)
            if self.DISTRO == "debian":
                run(
                    cmd_args=["sudo", "apt", "install", "-y", file_path],
                    msg="when trying to install vivaldi browser in /tmp",
                )

            elif self.DISTRO == "redhat":
                run(
                    cmd_args=["sudo", "rpm", "-ivh", file_path],
                    msg="when trying to install vivaldi browser in /tmp",
                )
            """
            with open(
                "/usr/share/applications/vivaldi-stable.desktop",
                "w+",
                encoding="utf-8",
            ) as vivaldi_lnk:
                lnk_file_content: list[str] = vivaldi_lnk.readlines()

                for line in lnk_file_content:
                    if not search("Exec=/usr/bin/vivaldi-stable", line):
                        continue

                    line = line.replace(
                        "Exec=/usr/bin/vivaldi-stable",
                        "Exec=/usr/bin/vivaldi-stable --no-sandbox",
                    )
                    break

                vivaldi_lnk.writelines(vivaldi_lnk)"""

            run(
                cmd_args=[
                    "sed",
                    "-i",
                    "s@Exec=/usr/bin/vivaldi-stable@& --no-sandbox@g",
                    "/usr/share/applications/vivaldi-stable.desktop",
                ],
                msg="when adding no-sandbox to vivaldi",
            )
