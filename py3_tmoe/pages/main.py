from py3_tmoe.pages.browser import run as browser
from py3_tmoe.pages.devtools import run as devtools
from py3_tmoe.ui.selection import Selection


def run():
    selection = Selection(
        idlist=["browser", "devtools"],
        itemlist=[
            ":globe_with_meridians: 浏览器：畅游互联网的海洋",
            ":wrench: IDE & 编辑器：Build your dreams",
        ],
        dialog_title="👏 欢迎来到PY Apps！",
    ).run()

    match selection:
        case "browser":
            browser()
        case "devtools":
            devtools()
