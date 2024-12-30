"""
This module contains an Firefox managing class
"""

from os import path
from enum import Enum
from subprocess import CalledProcessError, run
from time import sleep

from rich.console import Console

from ...utils.utils import get_distro_short_name

console = Console()


class FirefoxVariants(Enum):
    """
    The variants enum for firefox
    """

    FIREFOX = "firefox"
    ESR = "esr"


class Firefox:
    """
    The class for managing firefox

    Params:
        variant: the variant for firefox

    Type:
        variant: FirefoxVariants
    """

    DISTRO = get_distro_short_name()

    def __init__(self, variant: FirefoxVariants) -> None:
        self.variant = variant
        self.dependency_main: str = ""
        self.dependency_others: str = ""

    def setup_ppa_env(self):
        """
        Setup environment for PPA
        """
        if not path.exists("/usr/bin/add-apt-repository"):
            try:
                sleep(0.5)
                run(["apt", "update", "-y"], check=True)
                sleep(0.5)
                console.print(
                    "[green]apt[/green] [yellow]install[/yellow]",
                    " software-properties-common [cyan]-y[/cyan]",
                )
                run(["apt", "install", "software-properties-common", "-y"], check=True)
            except CalledProcessError as e:
                print(
                    "\033[91m\033[1m[Error]\033[0m",
                    " Error when installing software-properties-common for ppa",
                )
                print(f"\033[31mError message\033[0m\n\t{e.output}")

    def prepare(self):
        """
        Prepare the environment for installation
        """
        if self.variant == FirefoxVariants.ESR:
            self.dependency_main = "firefox-esr"
            self.dependency_others = "firefox-esr-locale-zh-hans"
        elif self.variant == FirefoxVariants.FIREFOX:
            # TODO: get firefox implemented
            pass

        if self.DISTRO in ["debian", "ubuntu"]:
            self.dependency_others += " ffmpeg"
            if self.DISTRO == "ubuntu":
                self.setup_ppa_env()
                try:
                    run(
                        ["sudo", "add-apt-repository", "ppa:mozillateam/ppa", "-y"],
                        check=True,
                    )
                except CalledProcessError as e:
                    print(
                        "\033[91m\033[1m[Error]\033[0m",
                        " Error occurred when trying to add mozilla PPA to the system",
                    )
                    print(f"\033[31mError message\033[0m\n\t{e.output}")
        elif self.DISTRO == "arch":
            self.dependency_others += " firefox-i18n-zh-cn firefox-i18n-zh-tw"
        elif self.DISTRO == "gentoo":
            self.dependency_main = "www-client/firefox"
            self.dependency_others = ""
        elif self.DISTRO == "suse":
            try:
                run(["dispatch-conf"], check=True)
            except CalledProcessError as e:
                print("\033[91m\033[1m[Error]\033[0m Error when running dispatch-conf")
                print(f"\033[31mError message\033[0m\n\t{e.output}")
            self.dependency_main = "MozillaFirefox-esr"
            self.dependency_others = "MozillaFirefox-esr-translations-common"

    def install(self):
        """
        The installation method of firefox
        """
        pass


# Firefox(variant=FirefoxVariants.FIREFOX).setup_ppa_env()

print(__package__)
