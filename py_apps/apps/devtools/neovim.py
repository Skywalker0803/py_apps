"""
Neovim config & setup class
"""

from enum import Enum, unique
from os import getenv
from re import search
from sys import exit as sys_exit

from py_apps.utils.app_manage import install_app
from py_apps.utils.cmd import run
from py_apps.utils.network import download, get, get_github_releases
from py_apps.utils.sys import check_architecture, get_distro_short_name


@unique
class NvimVariants(Enum):
    """Neovim different configs"""

    LAZY = "lazy"
    LUNAR = "lunar"
    ASTRO = "astro"
    SPACE = "space"
    NVCHAD = "nvchad"
    DEFAULT = "default"


class Neovim:
    """
    Neovim config & setup
    """

    _ARCH = check_architecture()
    _DISTRO, _OTHER_DISTRO = get_distro_short_name()

    def __init__(self, variant: NvimVariants) -> None:
        self.variant = variant

        # Neovim for Debian is too stale for these vim configs
        self.use_sys_pkg: bool = f"{self._DISTRO}_{self._ARCH}" not in [
            "debian_amd64",
            "debian_arm64",
        ]

        self.pkg = "neovim"

        # Setup nvim configs using git repos
        self.var_url: str = {
            NvimVariants.ASTRO: "https://github.com/AstroNvim/template",
            NvimVariants.LAZY: "https://github.com/LazyVim/starter",
            NvimVariants.NVCHAD: "https://github.com/NvChad/starter",
        }.get(self.variant, "")

        self.use_installer: str = ""

        # Setup nvim configs using installer scripts
        if self.var_url == "" and variant != NvimVariants.DEFAULT:
            self.use_installer = get(
                {
                    NvimVariants.LUNAR: "https://raw.githubusercontent.com/LunarVim/LunarVim/"
                    + "release-1.4/neovim-0.9/utils/installer/install.sh",
                    NvimVariants.SPACE: "https://spacevim.org/cn/install.sh",
                }.get(self.variant, "")
            ).text

            if self.use_installer == "":
                sys_exit("Unknown Variant")

    def prepare(self):
        """Prepare for the installation to go"""

        # If pkg is too stale
        if not self.use_sys_pkg:
            pkg_url: str = ""

            for url in get_github_releases("Skywalker0803/nvim-releases"):
                pkg_url = url if search(f".{self._ARCH}.deb", url) else ""

            download(pkg_url, file_path="/tmp/neovim.deb", overwrite=True)
        return self

    def install(self):
        """Install nvim with configs"""

        if self.use_sys_pkg:
            install_app(self._DISTRO, [self.pkg])

        else:
            run(
                ["sudo", "apt", "install", "/tmp/neovim.deb", "-y"],
                msg="when installing neovim pkg",
            )

        # Run installer
        if self.use_installer:
            run(["bash", "-c", self.use_installer], "when executing installer")

        # Clone the config repo
        elif self.var_url != "":
            run(["git", "clone", self.var_url, f"{getenv('HOME')}/.config/nvim"])
