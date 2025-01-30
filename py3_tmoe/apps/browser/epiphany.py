"""
This is the module for Epiphany Browser (A.K.A. GNOME Web)
"""

from py3_tmoe.apps.browser.common import Browser
from py3_tmoe.errors.distro_x_only import DistroXOnlyError
from py3_tmoe.utils.app_manage import install_app
from py3_tmoe.utils.sys import check_architecture, get_distro_short_name


class Epiphany(Browser):
    """Epiphany (GNOME Web)"""

    _ARCH: str = check_architecture()
    _DISTRO, _OTHER_DISTRO = get_distro_short_name()

    def __init__(self) -> None:
        self.pkg: str = ""
        self._pkg_dict: dict[str, str] = {
            "debian": "epiphany-browser",
            "redhat": "epiphany",
            "arch": "epiphany",
            "gentoo": "www-client/epiphany",
            "void": "epiphany",
        }

    def prepare(self) -> Browser:
        self.pkg = self._pkg_dict.get(self._DISTRO, "")

        if self.pkg == "":
            raise DistroXOnlyError(
                self._DISTRO,
                "Debian & RHEL & Archlinux & Gentoo & Void Linux",
            )
        return self

    def install(self) -> Browser:
        install_app(self._DISTRO, [self.pkg])
        return self
