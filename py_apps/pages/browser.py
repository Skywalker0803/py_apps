"""
Index for browser page
"""

from sys import exit as sys_exit

from py_apps.apps.browser.epiphany import Epiphany
from py_apps.apps.browser.falkon import Falkon
from py_apps.apps.browser.firefox import Firefox
from py_apps.apps.browser.firefox import FirefoxVariants
from py_apps.apps.browser.midori import Midori
from py_apps.apps.browser.vivaldi import Vivaldi
from py_apps.errors.distro_x_only import DistroXOnlyError
from py_apps.ui.dialog import Dialog
from py_apps.ui.selection import Selection


def run() -> bool:
    """
    Run browser selection page
    """
    selection = Selection(
        idlist=["firefox", "vivaldi", "midori", "epiphany", "falkon", "back"],
        itemlist=[
            ":fox_face: Firefox 浏览器：为自由而生",
            ":violin: Vivaldi 浏览器：一切皆可定制",
            ":leafy_green: Midori 浏览器：基于Gecko的轻量级开源浏览器",
            ":globe_with_meridians: GNOME Web：GNOME自带，又称Epiphany",
            ":eagle: Falkon：KDE系软件，基于QtWebEngine",
            "返回上级菜单",
        ],
        dialog_title="君欲何求：选择什么浏览器",
    )
    result = selection.run()

    match result:
        case "firefox":
            choose: str | None = Dialog(
                idlist=["firefox", "esr"],
                itemlist=["Firefox 火狐浏览器", "Firefox ESR 长期支持版"],
                dialog_title="Firefox 还是 ESR ？",
            ).run()

            opt: FirefoxVariants = FirefoxVariants.ESR

            if choose == "firefox":
                opt = FirefoxVariants.FIREFOX

            elif choose == "esr":
                opt = FirefoxVariants.ESR

            else:
                print(f"BUG in {__package__}")
                sys_exit(f"BUG in {__package__}")

            Firefox(variant=opt).prepare().install()
        case "vivaldi":
            try:
                Vivaldi().prepare().install()
            except DistroXOnlyError as err:
                print(str(err))
                sys_exit("distro x only err")
        case "midori":
            Midori().prepare().install()

        case "epiphany":
            Epiphany().prepare().install()
        case "falkon":
            Falkon().prepare().install()
        case _:
            return True

    return False


def browser():
    while True:
        if run():
            return
