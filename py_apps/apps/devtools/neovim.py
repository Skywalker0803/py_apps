"""
Neovim config & setup class
"""

from enum import Enum, unique


from py_apps.utils.cmd import run
from py_apps.utils.sys import check_architecture, get_distro_short_name
from py_apps.utils.network import get, get_github_releases


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

        # Setup nvim configs using installer scripts
        if self.var_url == "":
            self.use_installer: str = get(
                {
                    NvimVariants.LUNAR: "https://raw.githubusercontent.com/LunarVim/LunarVim/release-1.4/neovim-0.9/utils/installer/install.sh",
                    NvimVariants.SPACE: "https://spacevim.org/cn/install.sh",
                }.get(self.variant, "")
            ).text

            if self.use_installer != "":
                exit("Unknown Variant")

    def prepare(self):
        if self.use_installer:
            run(
                ["bash", "-c", self.use_installer],
                "when executing installer",
            )

        if not self.use_sys_pkg:
            get_github_releases("Skywalker0803/nvim-releases", "v0.11.0")
        return self
