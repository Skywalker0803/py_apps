"""
Install Midori open source browser
"""

from re import search
from sys import exit as sys_exit

from py3_tmoe.apps.browser.common import Browser
from py3_tmoe.errors.distro_x_only import DistroXOnlyError
from py3_tmoe.errors.unsupported_arch import UnsupportedArchitectureError
from py3_tmoe.utils.cmd import run
from py3_tmoe.utils.network import download, get_github_releases
from py3_tmoe.utils.sys import check_architecture, get_distro_short_name


class Midori(Browser):
    """
    This the class for managing Midori installation
    """

    _DISTRO, _OTHER_DISTRO = get_distro_short_name()

    _ARCH = check_architecture()
    _DISTRO, _OTHER_DISTRO = get_distro_short_name()

    def __init__(self) -> None:
        self.repo_path: str = "goastian/midori-desktop"
        self.pkg_link: str = ""

    def prepare(self) -> Browser:
        releases: list[str] = get_github_releases(self.repo_path)

        match self._DISTRO:
            case "debian":
                for i in releases:
                    if (search("._arm64[.]deb", i) and self._ARCH == "arm64") or (
                        search("._amd64[.]deb", i) and self._ARCH == "amd64"
                    ):
                        self.pkg_link = i
                        break

            case "redhat":
                for i in releases:
                    if search(".[.]x86_64[.]rpm", i) and self._ARCH == "amd64":
                        self.pkg_link = i
                        break

            case "arch":
                for i in releases:
                    if search(".x86_64[.]pkg[.]tar[.]zst", i):
                        self.pkg_link = i
                        break

            case _:
                raise DistroXOnlyError(
                    self._DISTRO,
                    "debian arm64/amd64 & redhat amd64 & arch amd64",
                )

        if self.pkg_link == "":
            raise UnsupportedArchitectureError(self._ARCH)

        return self

    def install(self) -> Browser:
        print(self.pkg_link)

        file_path: str = f"/tmp/midori.{self.pkg_link[-3:-1]+self.pkg_link[-1]}"

        install_err_msg: str = f"when trying to install midori package in {file_path}"

        download(self.pkg_link, file_path, overwrite=True)

        match self._DISTRO:
            case "debian":
                run(["sudo", "apt", "install", "-y", file_path], msg=install_err_msg)
            case "redhat":
                run(["sudo", "rpm", "-ivh", file_path], msg=install_err_msg)
            case "arch":
                run(
                    ["sudo", "pacman", "-U", "--noconfirm", "--needed"],
                    msg=install_err_msg,
                )

            case _:
                sys_exit(f"BUG in midori installer class at {__package__}")

        return self
