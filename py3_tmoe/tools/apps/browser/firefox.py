"""
This module contains an Firefox managing class
"""

from enum import Enum
from os import path
from time import sleep

from py3_tmoe.tools.utils.app_manage import install_app
from py3_tmoe.tools.utils.utils import get_distro_short_name, run


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
        FirefoxVariants variant: the variant for firefox
    """

    DISTRO: str = get_distro_short_name()[0]
    OTHER_DISTRO: str = get_distro_short_name()[1]

    def __init__(self, variant: FirefoxVariants) -> None:
        self.variant = variant
        self.dependency_main: str = ""
        self.dependency_others: list[str] = []

    def _setup_ppa_env(self) -> None:
        """
        Setup environment for PPA
        """
        if not path.exists("/usr/bin/add-apt-repository"):
            sleep(0.5)
            run(cmd_args=["apt", "update", "-y"], msg="when updating apt index")
            sleep(0.5)
            run(
                ["apt", "install", "software-properties-common", "-y"],
                msg="when installing software-properties-common for ppa",
            )

    def _prepare_for_esr(self) -> None:
        """
        Prepare the environment for the installation of firefox-esr
        """
        dep_main_dict: dict[str, str] = {
            "debian": "firefox-esr",
            "arch": "firefox-esr",
            "gentoo": "www-client/firefox",
            "suse": "MozillaFirefox-esr",
        }
        dep_others_dict: dict[str, list[str]] = {
            "debian": ["ffmpeg", "firefox-esr-locale-zh-hans"],
            "arch": ["firefox-i18n-zh-cn", "ffmpeg"],
            "suse": ["MozillaFirefox-esr-translations-common"],
        }
        self.dependency_main = dep_main_dict.get(self.DISTRO, "")
        self.dependency_others = dep_others_dict.get(self.OTHER_DISTRO, [])

        if self.OTHER_DISTRO == "ubuntu":
            self._setup_ppa_env()
            run(
                cmd_args=[
                    "sudo",
                    "add-apt-repository",
                    "ppa:mozillateam/ppa",
                    "-y",
                ],
                msg="when trying to add mozilla PPA to the system",
            )

        if self.DISTRO == "gentoo":
            run(cmd_args=["dispatch-conf"], msg="when running dispatch-conf")

    def _set_ubuntu_firefox_priority(self) -> None:
        """
        This function tends to disable snap firefox by default in ubuntu
        """
        with open(
            file="/etc/apt/preferences.d/90-mozilla-firefox", mode="w", encoding="utf-8"
        ) as apt_conf_file:
            apt_conf_file.writelines(
                """Package: *
Pin: release o=LP-PPA-mozillateam,l=Firefox ESR and Thunderbird stable builds
Pin-Priority: 900
""".split("\n", maxsplit=1)
            )
            run(
                ["chmod", "a+r", "-vf", "/etc/apt/preferences.d/90-mozilla-firefox"],
                msg='when trying to give permission to "/etc/apt/preferences.d/90-mozilla-firefox"',
            )

    def _prepare_for_firefox(self) -> None:
        """
        Prepare the environment for the installation of firefox
        """
        dep_main_dict: dict[str, str] = {
            "debian": "firefox",
            "arch": "firefox",
            "redhat": "firefox",
            "gentoo": "www-client/firefox-bin",
            "suse": "MozillaFirefox",
        }
        dep_others_dict: dict[str, list[str]] = {
            "debian": ["firefox-l10n-zh-cn"],
            "arch": ["firefox-i18n-zh-cn", "firefox-i18n-zh-tw"],
            "suse": ["MozillaFirefox-translations-common"],
        }
        self.dependency_main = dep_main_dict.get(self.DISTRO, "")
        self.dependency_others = dep_others_dict.get(self.DISTRO, [])

        if self.OTHER_DISTRO == "ubuntu":
            self.dependency_others = ["ffmpeg", "^firefox-locale-zh-cn"]

        if self.DISTRO == "gentoo":
            run(cmd_args=["dispatch-conf"], msg="when running dispatch-conf")

    def prepare(self) -> None:
        """
        Prepare for firefox installation
        """
        if self.variant == FirefoxVariants.FIREFOX:
            self._prepare_for_firefox()
        elif self.variant == FirefoxVariants.ESR:
            self._prepare_for_esr()

    def _install_for_esr(self) -> None:
        """
        Installation for ESR
        """
        install_app(
            distro=self.DISTRO,
            app=self.dependency_main,
            app_dep_str=" ".join(self.dependency_others),
        )
        if (not path.exists("/usr/bin/firefox")) and (
            not path.exists("/usr/bin/firefox-esr")
        ):
            self._install_for_firefox()
        else:
            if self.DISTRO == "debian":
                package: str = "firefox-esr"
                run(
                    cmd_args=[
                        "sed",
                        "-i",
                        "-E",
                        "'s@(configure)@pre\\1@'",
                        f"/var/lib/dpkg/info/{package}.postinst",
                    ],
                    msg="when changing configure to preconfigure in"
                    + f"/var/lib/dpkg/info/{package}.postinst",
                )
                run(
                    cmd_args=["sudo", "dpkg", "--configure", "-a"],
                    msg="when trying to fix misconfigured deb packages",
                )

    def _install_for_firefox(self) -> None:
        """
        Installation for firefox
        """
        install_app(
            distro=self.DISTRO,
            app=self.dependency_main,
            app_dep_str=" ".join(self.dependency_others),
        )
        if not path.exists("/usr/bin/firefox"):
            self._install_for_esr()
        else:
            if self.DISTRO == "debian":
                package: str = "firefox"
                run(
                    cmd_args=[
                        "sed",
                        "-i",
                        "-E",
                        "'s@(configure)@pre\\1@'",
                        f"/var/lib/dpkg/info/{package}.postinst",
                    ],
                    msg="when changing configure to preconfigure in"
                    + f"/var/lib/dpkg/info/{package}.postinst",
                )
                run(
                    cmd_args=["sudo", "dpkg", "--configure", "-a"],
                    msg="when trying to fix misconfigured deb packages",
                )

    def install(self) -> None:
        """
        The installation method of firefox

        Usage: this method MUST be used after prepare() method!!!
            firefox = Firefox(variant=FirefoxVariants.ESR)
            firefox.prepare()
            firefox.install()
        """
        if self.DISTRO == FirefoxVariants.ESR:
            self._install_for_esr()
        elif self.DISTRO == FirefoxVariants.FIREFOX:
            self._install_for_firefox()
