"""
项目的main模块
"""

from py3_tmoe.apps.browser.vivaldi import Vivaldi
from py3_tmoe.errors.distro_x_only import DistroXOnlyError

from .ui.selection import Selection


app: Selection = Selection(
    idlist=["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n"],
    itemlist=[
        "Vivaldi browser",
        "b",
        "c",
        "d",
        "e",
        "f",
        "g",
        "h",
        "i",
        "j",
        "k",
        "l",
        "m",
        "n",
    ],
    dialogTitle="Main应用",
)
res = app.run()
print(res)

if res == "a":
    vivaldi = Vivaldi()
    try:
        vivaldi.prepare()
        vivaldi.install()
    except DistroXOnlyError as err:
        print(str(err))
