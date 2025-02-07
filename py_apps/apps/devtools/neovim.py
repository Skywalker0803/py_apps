"""
Neovim config & setup class
"""

from enum import Enum, unique

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
        use_sys_pkg_dict: dict[str, bool] = {
            "debian_arm64": False,
            "debian_amd64": False,
        }
        self.variant = variant
        self.use_sys_pkg: bool = use_sys_pkg_dict.get(
            f"{self._DISTRO}_{self._ARCH}", True
        )

    def prepare(self):
        self.pkg = "neovim"
        return self
