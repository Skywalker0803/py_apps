"""PY Apps front page"""

import sys

from py_apps.pages.browser import browser
from py_apps.pages.common import loop
from py_apps.pages.devtools import devtools
from py_apps.ui.selection import Selection


def run() -> bool:
    """Main page function"""

    selection = Selection(
        idlist=["browser", "devtools", "quit"],
        itemlist=[
            ":globe_with_meridians: 浏览器：畅游互联网的海洋",
            ":wrench: IDE & 编辑器：Build your dreams",
            "退出",
        ],
        dialog_title="👏 欢迎来到PY Apps！",
    ).run()

    match selection:
        case app_type if app_type in ["browser", "devtools"]:
            loop({"browser": browser, "devtools": devtools}[app_type])

        case _:
            return True

    return False


def main():
    """Main loop for the app"""

    while True:
        if run():
            print("exit")
            break
    sys.exit()
