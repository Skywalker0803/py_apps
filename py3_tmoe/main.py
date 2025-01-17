"""
项目的main模块
"""

from py3_tmoe.apps.browser.firefox import FirefoxVariants, Firefox

firefox = Firefox(FirefoxVariants.ESR)

firefox.prepare()
firefox.install()
