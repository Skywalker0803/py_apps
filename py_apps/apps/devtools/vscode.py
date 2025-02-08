"""VSCode"""

from py_apps.utils.cmd import run
from py_apps.utils.network import download
from py_apps.utils.sys import check_architecture, get_distro_short_name
from py_apps.utils.utils import fix_electron_libxssl


class VSCode:
    """Visual Studio Code: Editor Evolved"""

    _ARCH: str = check_architecture()
    _DISTRO, _OTHER_DISTRO = get_distro_short_name()

    def __init__(self) -> None:
        self.pkg_url: str = ""
        # Set pkg dict to some Microsoft direct links
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
        """Prepare for vscode"""
        self.pkg_url = self._pkg_dict.get(
            (self._DISTRO if self._DISTRO in ["debian", "redhat"] else "other")
            + "_"
            + self._ARCH,
            "",
        )

        # Decide which suffix to use based on current distro
        suffix: str = {"debian": "deb", "redhat": "rpm"}.get(self._DISTRO, "tar.gz")

        self.pkg_file_path = f"/tmp/vscode.{suffix}"

        # Download the pkg
        download(self.pkg_url, self.pkg_file_path, overwrite=True)

        return self

    def install(self):
        """Install vscode pkg"""
        fix_electron_libxssl(self._DISTRO)
        # TODO: FIX VSCode for distros other than deb & rhel

        # Install pkg for deb and rhel
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
