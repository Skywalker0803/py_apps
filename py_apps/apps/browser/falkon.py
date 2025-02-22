"""
Falkon Browser
"""

from os import path

from py_apps.apps.browser.common import Browser
from py_apps.errors.distro_x_only import DistroXOnlyError
from py_apps.ui.notice import Notice
from py_apps.utils.app_manage import install_app
from py_apps.utils.cmd import run
from py_apps.utils.sys import check_architecture, get_distro_short_name


class Falkon(Browser):
    """Falkon Browser"""

    _ARCH: str = check_architecture()
    _DISTRO, _OTHER_DISTRO = get_distro_short_name()

    def __init__(self) -> None:
        self.pkg: str = ""
        self._pkg_dict: dict[str, str] = {
            "debian": "falkon",
            "redhat": "falkon",
            "arch": "falkon",
            "gentoo": "www-client/falkon",
            "void": "falkon",
        }

    def prepare(self) -> Browser:
        self.pkg = self._pkg_dict.get(self._DISTRO, "")
        if self.pkg == "":
            raise DistroXOnlyError(
                self._DISTRO,
                "Debian & RHEL & Archlinux & Void Linux & Gentoo",
            )

        return self

    def install(self) -> Browser:
        install_app(self._DISTRO, [self.pkg])

        bin_path = f"{path.dirname(__file__)}/lnk/falkon-no-sandbox"
        lnk_path = f"{path.dirname(__file__)}/lnk/org.kde.falkon-no-sandbox.desktop"

        # Write falkon no sandbox command
        with open(
            "/usr/local/bin/falkon-no-sandbox", mode="w", encoding="utf-8"
        ) as falkon_no_sandbox:
            cmd_bin_content = []
            with open(bin_path, mode="r", encoding="utf-8") as bin_file:
                cmd_bin_content = bin_file.readlines()

            falkon_no_sandbox.writelines(cmd_bin_content)
        run(["chmod", "+rwx", "-vf", "/usr/local/bin/falkon-no-sandbox"])

        # Write falkon no sandbox desktop entry
        with open(
            "/usr/share/applications/org.kde.falkon-no-sandbox.desktop",
            mode="w",
            encoding="utf-8",
        ) as entry:
            entry_content: list[str] = []
            with open(lnk_path, mode="r", encoding="utf-8") as lnk:
                entry_content = lnk.readlines()

            entry.writelines(entry_content)
        run(
            [
                "chmod",
                "+rwx",
                "-vf",
                "/usr/share/applications/org.kde.falkon-no-sandbox.desktop",
            ]
        )

        notice = Notice("若不能使用Falkon，请启动falkon-no-sandbox").run()
        assert notice == "ok"

        return self
