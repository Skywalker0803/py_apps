"""
Falkon Browser
"""

from py3_tmoe.apps.browser.common import Browser


class Falkon(Browser):
    """Falkon Browser"""

    def __init__(self) -> None:
        self.pkg: str = "falkon"

    def prepare(self) -> Browser:
        return self

    def install(self) -> Browser:
        return self
