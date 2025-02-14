"""Class for Jetbrains IDE Family"""

from enum import Enum, unique


from bs4 import BeautifulSoup

from py_apps.utils.network import get
from py_apps.utils.utils import fetch_webpage_content


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

        self.page: str = f"https://www.jetbrains.com/{self.product}/download"

        self.link = ""

    def prepare(self):
        # soup: BeautifulSoup = BeautifulSoup(get(self.page).text, "html.parser")
        soup = fetch_webpage_content(self.page)

        if soup is None:
            raise Exception("")
        links = soup.find_all(
            "a",
            {
                # "class": "linux-download-link",
                # "data-product": self.product,
                # "data-type": self.edition,
            },
        )

        for element in links:
            self.link = element["href"] if links else None

        if self.link is None:
            raise Exception("Bug in Jetbrains get download link")

        print(links)
        print(type(links))
        print(self.link)

        return self
