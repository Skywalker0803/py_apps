"""
Falkon Browser
"""

from py3_tmoe.apps.browser.common import Browser
from py3_tmoe.utils.sys import check_architecture, get_distro_short_name


class Falkon(Browser):
    """Falkon Browser"""

    _ARCH: str = check_architecture()
    _DISTRO, _OTHER_DISTRO = get_distro_short_name()

    def __init__(self) -> None:
        self.pkg: str = ""

    def prepare(self) -> Browser:
        match self._DISTRO:
            case "debian":
                self.pkg = "falkon"

        return self

    def install(self) -> Browser:
        return self
