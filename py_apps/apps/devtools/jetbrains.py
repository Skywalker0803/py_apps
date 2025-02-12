"""Class for Jetbrains IDE Family"""

from enum import Enum, unique


@unique
class JetbrainsVarianta(Enum):
    IDEA_COMMUNITY = "idea_community"
    PYCHARM_COMMUNITY = "pycharm_community"


class Jetbrains:
    """Jetbrains IDE Family Classes"""

    def __init__(self) -> None:
        self.page: str = ""
