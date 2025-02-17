"""Class for Jetbrains IDE Family"""

from enum import Enum, unique


from py_apps.utils.sys import check_architecture


@unique
class JetbrainsVariants(Enum):
    """JetbrainsVariants enum list"""

    IDEA_COMMUNITY = "idea_community"
    IDEA_PRO = "idea_professional"
    PYCHARM_COMMUNITY = "python_community"
    PYCHARM_PRO = "python_professional"
    GOLAND = "go"
    PHPSTORM = "webide"
    CLION = "cpp"
    RIDER = "rider"
    RUSTROVER = "rustrover"
    RUBYMINE = "ruby"


class Jetbrains:
    """Jetbrains IDE Family Classes"""

    _ARCH = check_architecture()

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
        """Prepare download links"""

        file_name: str = {
            "idea_community": "ideaIC",
            "idea_professional": "ideaU",
            "python_community": "pycharm-community",
            "python_professional": "pycharm-professional",
            "go": "goland",
            "webide": "PhpStorm",
            "webstorm": "WebStorm",
            "cpp": "CLion",
            "rider": "JetBrains.Rider",
            "rustrover": "RustRover",
            "ruby": "RubyMine",
        }[self.variant.value]

        version: str = {
            "idea": "2024.3.2.1",
            "python": "2024.3.3",
            "go": "2024.3.3",
            "webide": "2024.3.3",
            "webstorm": "2024.3.2.1",
            "cpp": "2024.3.3",
            "rider": "2024.3.5",
            "rustrover": "2024.3.4",
            "ruby": "2024.3.2.1",
        }[self.product]

        self.link = (
            f"https://download.jetbrains.com/{self.product}/"
            + f"{file_name}-{version}"
            + ("-aarch64" if self._ARCH == "arm64" else "")
            + ".tar.gz"
        )

        # print(self.link)

        return self
