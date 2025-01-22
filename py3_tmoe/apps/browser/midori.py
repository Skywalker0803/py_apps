"""
Install Midori open source browser
"""

from py3_tmoe.apps.browser.common import Browser
from py3_tmoe.utils.download import get_github_releases
from py3_tmoe.utils.utils import get_distro_short_name


class Midori(Browser):
    """
    This the class for managing Midori installation
    """

    _DISTRO, _OTHER_DISTRO = get_distro_short_name()

    def __init__(self) -> None:
        pass

    def prepare(self) -> Browser:
        return self

    def install(self) -> Browser:
        print("\n".join(get_github_releases("goastian/midori-desktop")))
        return self
