"""Class for Jetbrains IDE Family"""

from enum import Enum, unique


from bs4 import BeautifulSoup

from py_apps.utils.network import get
from py_apps.utils.utils import fetch_webpage_content


jetbrains_ver: dict[str, str] = {
    "idea": "2024.3.2.1",
}


@unique
class JetbrainsVariants(Enum):
    IDEA_COMMUNITY = "idea_community"
    IDEA_PRO = "idea_professional"
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

    def __init__(self, variant: JetbrainsVariants) -> None:
        self.variant = variant
        self.product: str = variant.value.split("_")[0]
        self.edition: str | None = (
            variant.value.split("_")[-1]
            if self.product != self.variant.value.split("_")[-1]
            else None
        )

        # self.page: str = f"https://www.jetbrains.com/{self.product}/download"

        self.link = ""

    def prepare(self):
        file_name = {"idea_community": "ideaIC", "idea_professional": "ideaU"}[
            self.variant.value
        ]

        self.link = f"https://download.jetbrains.com/{self.product}/{file_name}-{jetbrains_ver[self.product]}{''}.tar.gz"

        if self.link is None:
            raise Exception("Bug in Jetbrains get download link")

        print(self.link)

        return self
