"""
项目的main模块
"""

from py3_tmoe.apps.browser.firefox import Firefox, FirefoxVariants


firefox = Firefox(FirefoxVariants.FIREFOX)

firefox.prepare()
firefox.install()
