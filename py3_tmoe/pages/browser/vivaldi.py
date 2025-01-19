"""
Vivaldi install
"""

from py3_tmoe.apps.browser.vivaldi import Vivaldi
from py3_tmoe.errors.distro_x_only import DistroXOnlyError


def install_vivaldi() -> None:
    """
    Install vivaldi
    """
    vivaldi: Vivaldi = Vivaldi()
    try:
        vivaldi.prepare()
        vivaldi.install()
    except DistroXOnlyError as err:
        print(str(err))
