"""
This is the module for Epiphany Browser (A.K.A. GNOME Web)
"""

from py3_tmoe.utils.sys import check_architecture, get_distro_short_name

from .common import Browser


class Epiphany(Browser):
    """Epiphany (GNOME Web)"""

    _ARCH: str = check_architecture()
    _DISTRO, _OTHER_DISTRO = get_distro_short_name()

    def __init__(self) -> None:
        self.pkg: str = ""

    def prepare(self) -> Browser:
        match self._DISTRO:
            case "debian":
                self.pkg = "epiphany-browser"
            case "redhat":
                self.pkg = "epiphany"
            case "arch":
                self.pkg = "epiphany"
            case "gentoo":
                self.pkg = "www-client/epiphany"
        return self

    def install(self) -> Browser:
        return self
