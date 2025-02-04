"""VSCode"""

from py3_tmoe.utils.cmd import run
from py3_tmoe.utils.network import download
from py3_tmoe.utils.sys import check_architecture, get_distro_short_name
from py3_tmoe.utils.utils import fix_electron_libxssl


class VSCode:
    """Visual Studio Code: Editor Evolved"""

    _ARCH: str = check_architecture()
    _DISTRO, _OTHER_DISTRO = get_distro_short_name()

    def __init__(self) -> None:
        self.pkg_url: str = ""
        self._pkg_dict: dict[str, str] = {
            "debian_amd64": "https://go.microsoft.com/fwlink/?LinkID=760868",
            "redhat_amd64": "https://go.microsoft.com/fwlink/?LinkID=760867",
            "other_amd64": "https://go.microsoft.com/fwlink/?LinkID=620884",
            "debian_arm64": "https://aka.ms/linux-arm64-deb",
            "redhat_arm64": "https://aka.ms/linux-arm64-rpm",
            "other_arm64": "https://aka.ms/linux-arm64",
            "debian_armhf": "https://aka.ms/linux-armhf-deb",
            "redhat_armhf": "https://aka.ms/linux-armhf-rpm",
            "other_armhf": "https://aka.ms/linux-armhf",
        }

    def prepare(self):
        self.pkg_url = self._pkg_dict.get(
            (self._DISTRO if self._DISTRO in ["debian", "redhat"] else "other")
            + "_"
            + self._ARCH,
            "",
        )
        suffix: str = {"debian": "deb", "redhat": "rpm"}.get(self._DISTRO, "tar.gz")

        self.pkg_file_path = f"/tmp/vscode.{suffix}"

        download(self.pkg_url, self.pkg_file_path, overwrite=True)

        return self

    def install(self):
        fix_electron_libxssl(self._DISTRO)
        # TODO: FIX VSCode for other distros

        run(
            {
                "debian": ["sudo", "apt", "install", self.pkg_file_path, "-y"],
                "redhat": ["sudo", "dnf", "install", self.pkg_file_path],
            }.get(
                self._DISTRO, ["tar", "-zxvf", self.pkg_file_path, "-C", "/usr/share/"]
            ),
            "installing vscode pkg in /tmp",
        )

        if self._DISTRO not in ["debian", "redhat"]:
            run(["rm", "-rvf", "/usr/share/code"])
        return self
