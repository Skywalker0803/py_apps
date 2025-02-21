"""
项目的main模块
"""

from py_apps.apps.devtools.jetbrains import Jetbrains, JetbrainsVariants
from py_apps.pages.main import run


Jetbrains(JetbrainsVariants.PHPSTORM).prepare().install()

run()
