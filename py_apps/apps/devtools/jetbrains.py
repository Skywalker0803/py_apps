"""Class for Jetbrains IDE Family"""

from enum import Enum, unique


@unique
class JetbrainsVarianta(Enum):
    IDEA_COMMUNITY = "idea_community"
    IDEA_PRO = "idea_pro"
    PYCHARM_COMMUNITY = "pycharm_community"
    PYCHARM_PRO = "pycharm_professional"
    GOLAND = "goland"
    PHPSTORM = "phpstorm"


class Jetbrains:
    """Jetbrains IDE Family Classes"""

    def __init__(self) -> None:
        self.page: str = ""
