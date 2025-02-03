"""VSCode"""

from py3_tmoe.utils.sys import check_architecture, get_distro_short_name


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
        return self

    def install(self):
        return self
