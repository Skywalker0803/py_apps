"""Class for Jetbrains IDE Family"""

from enum import Enum, unique


@unique
class JetbrainsVarianta(Enum):
    IDEA_COMMUNITY = "intellij-idea_community"
    IDEA_PRO = "intellij-idea_professional"
    PYCHARM_COMMUNITY = "pycharm_community"
    PYCHARM_PRO = "pycharm_professional"
    GOLAND = "goland"
    PHPSTORM = "phpstorm"
    CLION = "clion"
    RIDER = "rider"
    RUSTROVER = "rustrover"
    RUBYMINE = "rubymine"


class Jetbrains:
    """Jetbrains IDE Family Classes"""

    def __init__(self) -> None:
        self.page: str = ""
