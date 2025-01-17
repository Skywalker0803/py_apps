"""
项目的main模块
"""

from py3_tmoe.apps.browser.firefox import Firefox, FirefoxVariants


<<<<<<< Updated upstream
firefox = Firefox(FirefoxVariants.FIREFOX)

firefox.prepare()
firefox.install()
=======
app: Selection = Selection(
    idlist=["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n"],
    itemlist=["Vivaldi 浏览器：一切皆可定制", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n"],
    dialogTitle="Main应用",
)
res = app.run()
print(res, get_distro_short_name())

if res == "a":
    vivaldi=
>>>>>>> Stashed changes
