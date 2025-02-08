"""
Neovim config & setup class
"""

from enum import Enum, unique

from py_apps.utils.cmd import run
from py_apps.utils.sys import check_architecture, get_distro_short_name
from py_apps.utils.network import download, get


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
        use_sys_pkg_dict: dict[str, bool] = {
            "debian_arm64": False,
            "debian_amd64": False,
        }
        self.variant = variant
        self.use_sys_pkg: bool = use_sys_pkg_dict.get(
            f"{self._DISTRO}_{self._ARCH}", True
        )
        self.pkg = "neovim"

        self.var_url: str = {
            NvimVariants.ASTRO: "https://github.com/AstroNvim/template",
            NvimVariants.LAZY: "https://github.com/LazyVim/starter",
            NvimVariants.NVCHAD: "https://github.com/NvChad/starter",
        }.get(self.variant, "")

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
            download(self.use_installer, file_path="/tmp/installer.sh", overwrite=True)
            run(
                ["sudo", "chmod", "+rx", "/tmp/installer.sh"],
                "when granting executive permission to installer",
            )
        return self
