"""
Index for browser page
"""

from sys import exit as sys_exit

from py_apps.apps.browser.epiphany import Epiphany as _Epiphany
from py_apps.apps.browser.falkon import Falkon
from py_apps.apps.browser.firefox import Firefox as _Firefox
from py_apps.apps.browser.firefox import FirefoxVariants as _FirefoxVariants
from py_apps.apps.browser.midori import Midori as _Midori
from py_apps.apps.browser.vivaldi import Vivaldi as _Vivaldi
from py_apps.errors.distro_x_only import DistroXOnlyError as _DistroXOnlyError
from py_apps.ui.dialog import Dialog as _Dialog
from py_apps.ui.selection import Selection as _Selection


def run() -> None:
    """
    Run browser selection page
    """
    selection = _Selection(
        idlist=["firefox", "vivaldi", "midori", "epiphany", "falkon"],
        itemlist=[
            ":fox_face: Firefox 浏览器：为自由而生",
            ":violin: Vivaldi 浏览器：一切皆可定制",
            ":leafy_green: Midori 浏览器：基于Gecko的轻量级开源浏览器",
            ":globe_with_meridians: GNOME Web：GNOME自带，又称Epiphany",
            ":eagle: Falkon：KDE系软件，基于QtWebEngine",
        ],
        dialog_title="君欲何求：选择什么浏览器",
    )
    result = selection.run()

    match result:
        case "firefox":
            choose: str | None = _Dialog(
                idlist=["firefox", "esr"],
                itemlist=["Firefox 火狐浏览器", "Firefox ESR 长期支持版"],
                dialog_title="Firefox 还是 ESR ？",
            ).run()

            opt: _FirefoxVariants = _FirefoxVariants.ESR

            if choose == "firefox":
                opt = _FirefoxVariants.FIREFOX

            elif choose == "esr":
                opt = _FirefoxVariants.ESR

            else:
                print(f"BUG in {__package__}")
                sys_exit(f"BUG in {__package__}")

            _Firefox(variant=opt).prepare().install()
        case "vivaldi":
            try:
                _Vivaldi().prepare().install()
            except _DistroXOnlyError as err:
                print(str(err))
                sys_exit("distro x only err")
        case "midori":
            _Midori().prepare().install()

        case "epiphany":
            _Epiphany().prepare().install()
        case "falkon":
            Falkon().prepare().install()
        case _:
            print("TODO")
            sys_exit("todo")
