"""
Install Midori open source browser
"""

from py3_tmoe.utils.utils import get_distro_short_name
from py3_tmoe.utils.app_manage import install_app


class Midori:
    """
    This the class for managing Midori installation
    """

    _DISTRO, _OTHER_DISTRO = get_distro_short_name()

    def __init__(self) -> None:
        pass

    def prepare(self) -> None:
        pass

    def install(self) -> None:
        install_app(self._DISTRO, ["midori"])
