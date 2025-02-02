"""
Falkon Browser
"""

from py3_tmoe.apps.browser.common import Browser
from py3_tmoe.errors.distro_x_only import DistroXOnlyError
from py3_tmoe.utils.app_manage import install_app
from py3_tmoe.utils.sys import check_architecture, get_distro_short_name
from py3_tmoe.utils.cmd import run

from py3_tmoe.ui.notice import Notice


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

        with open(
            "/usr/local/bin/falkon-no-sandbox", mode="+w", encoding="utf-8"
        ) as falkon_no_sandbox:
            falkon_no_sandbox.writelines(
                [
                    "#!/usr/bin/env bash",
                    "###############",
                    "if [[ $(command -v falkon) ]]; then",
                    "   TMOE_BIN='falkon'",
                    "elif [[ $(command -v falkon-browser) ]]; then",
                    "   TMOE_BIN='falkon-browser'",
                    "elif [[ $(command -v org.kde.falkon) ]]; then",
                    "   TMOE_BIN='org.kde.falkon'",
                    "fi",
                    "",
                    'case "$(id -u)" in',
                    '0) exec ${TMOE_BIN} --no-sandbox "$@" ;;',
                    "*)",
                    '   ${TMOE_BIN} ${ADDITIONAL} "$@"',
                    '   case "$?" in',
                    "   0) ;;",
                    '   *) exec ${TMOE_BIN} --no-sandbox "$@" ;;',
                    "   esac",
                    "   ;;",
                    "esac",
                ]
            )
        run(["chmod", "+x", "-vf", "/usr/bin/falkon-no-sandbox"])

        notice = Notice("若不能使用Falkon，请启动falkon-no-sandbox").run()
        assert notice == "ok"

        return self
