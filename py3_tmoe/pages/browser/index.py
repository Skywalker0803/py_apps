"""
Index for browser page
"""

from py3_tmoe.apps.browser.midori import Midori
from py3_tmoe.pages.browser.firefox import firefox_or_esr as _firefox_or_esr
from py3_tmoe.pages.browser.vivaldi import install_vivaldi as _install_vivaldi
from py3_tmoe.ui.selection import Selection as _Selection


def run() -> None:
    """
    Run browsee selection page
    """
    selection = _Selection(
        idlist=["firefox", "vivaldi", "midori"],
        itemlist=[
            ":fox_face: Firefox 浏览器：为自由而生",
            ":violin: Vivaldi 浏览器：一切皆可定制",
            ":leafy_green: Midori 浏览器：基于Gecko的轻量级开源浏览器",
        ],
        dialogTitle="君欲何求：选择什么浏览器",
    )
    result = selection.run()

    match result:
        case "firefox":
            _firefox_or_esr()
        case "vivaldi":
            _install_vivaldi()
        case "midori":
            Midori().prepare().install()
        case _:
            print("TODO")
            exit(100)
