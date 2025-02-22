"""
Index for browser page
"""

from py_apps.apps.browser.epiphany import Epiphany
from py_apps.apps.browser.falkon import Falkon
from py_apps.apps.browser.firefox import Firefox, FirefoxVariants
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
        # Install for firefox
        case "firefox":
            choose: str | None = Dialog(
                idlist=["firefox", "esr"],
                itemlist=["Firefox 火狐浏览器", "Firefox ESR 长期支持版"],
                dialog_title="Firefox 还是 ESR ？",
            ).run()

            Firefox(
                FirefoxVariants(FirefoxVariants._value2member_map_[choose])
            ).prepare().install()

        # For other browsers
        case browser_variant if browser_variant in [
            "vivaldi",
            "midori",
            "epiphany",
            "falkon",
        ]:
            try:
                {
                    "vivaldi": Vivaldi,
                    "midori": Midori,
                    "epiphany": Epiphany,
                    "falkon": Falkon,
                }[browser_variant]().prepare().install()
            except DistroXOnlyError as err:
                print(str(err))
            except Exception as err:
                print(str(err))

        # Return to upper level
        case _:
            return True

    return False


def browser():
    """Browser page main loop"""

    while True:
        if run():
            return
