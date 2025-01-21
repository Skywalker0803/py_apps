"""
Install Midori open source browser
"""

from py3_tmoe.utils.download import get_github_releases
from py3_tmoe.utils.utils import get_distro_short_name


class Midori:
    """
    This the class for managing Midori installation
    """

    _DISTRO, _OTHER_DISTRO = get_distro_short_name()

    def __init__(self) -> None:
        pass

    def prepare(self):
        return self

    def install(self):
        print("\n".join(get_github_releases("goastian/midori-desktop")))
        return self
