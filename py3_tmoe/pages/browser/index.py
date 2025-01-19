"""
Index for browser page
"""

from py3_tmoe.pages.browser.firefox import firefox_or_esr as _firefox_or_esr
from py3_tmoe.pages.browser.vivaldi import install_vivaldi as _install_vivaldi
from py3_tmoe.ui.selection import Selection as _Selection


def run() -> None:
    """
    Run browsee selection page
    """
    selection = _Selection(
        idlist=["firefox", "vivaldi"],
        itemlist=["Firefox 浏览器：为自由而生", "Vivaldi 浏览器：一切皆可定制"],
        dialogTitle="君欲何求：选择什么浏览器",
    )
    result = selection.run()

    match result:
        case "firefox":
            _firefox_or_esr()
        case "vivaldi":
            _install_vivaldi()
