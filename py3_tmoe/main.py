"""
项目的main模块
"""

from .tools.utils.utils import get_distro_short_name
from .ui.selection import Selection


app: Selection = Selection(
    idlist=["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n"],
    itemlist=["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n"],
    dialogTitle="Main应用",
)
res = app.run()
print(res, get_distro_short_name())
