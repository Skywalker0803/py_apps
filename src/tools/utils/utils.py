"""
This module contains some basic util functions
"""

from csv import reader
from pathlib import Path
from re import search, sub


def to_snakecase(string: str) -> str:
    """
    Change the given string to the from of a_b_c (Snake Case)

    Params:
        string: the input string

    Type:
        string: str
    """
    return "_".join(
        sub(
            "([A-Z][a-z]+)", r" \1", sub("([A-Z]+)", r" \1", string.replace("-", " "))
        ).split()
    ).lower()


def get_distro_fullname() -> str:
    """
    Get the full name of current Linux distro (such as Ubuntu 22.04.5 LTS (Jammy Jellyfish))
    """
    release_data = {}

    with open("/etc/os-release", encoding="utf-8") as os_release:
        release_reader = reader(os_release, delimiter="=")
        for row in release_reader:
            if row:
                release_data[row[0]] = row[1]

        if release_data["ID"] in ["debian", "raspbian"]:
            with open("/etc/debian_version", encoding="utf-8") as debian_release:
                debian_version = debian_release.readline().strip()
                major_version = debian_version.split(".")[0]
            version_split = release_data["VERSION"].split(" ", maxsplit=1)
            if version_split[0] == major_version:
                # Just major version shown, replace it with the full version
                release_data["VERSION"] = " ".join([debian_version] + version_split[1:])

        return f"{release_data['NAME']} {release_data['VERSION']}"


distro_list: list[str] = [
    # Alpine
    "alpine",
    # Red hat
    "fedora",
    "Fedora",
    "CentOS",
    "Red Hat",
    "redhat",
    "rhel",
    # Archlinux
    "Arch",
    "Manjaro",
    # Debian
    "debian",
    "deepin",
    "uos.com",
    "ubuntu",
    "Kali",
    # Gentoo
    "gentoo",
    "funtoo",
    # Solus
    "Solus",
    # openSUSE
    "openSUSE",
    "suse",
]


def get_distro_short_name() -> list[str]:
    """
    Get the shortened version of current Linux distro name (such as ubuntu, debian)

    Returns: str
    """

    release_content = (
        Path("/etc/os-release").read_text(encoding="utf-8").replace("\n", " ")
    )

    distro: str = ""
    debian_distro: str = ""
    redhat_distro: str = ""
    for _distro in distro_list:
        if search(pattern=_distro, string=release_content):
            distro = _distro.replace(" ", "").lower()
            break

    if distro in ["debian", "ubuntu", "kali", "deepin", "uos.com"]:
        distro = "debian"
        debian_distro_list: list[str] = ["ubuntu", "Kali", "deepin", "uos.com"]
        for _distro in debian_distro_list:
            if search(pattern=_distro, string=release_content):
                debian_distro = _distro
                if debian_distro in ["deepin", "uos.com"]:
                    debian_distro = "deepin"
                break
    if distro == "manjaro":
        distro = "arch"

    if distro in ["fedora", "centos", "redhat"]:
        distro = "redhat"
        redhat_distro_list: list[str] = ["Fedora", "ID=centos", "ID=rhel"]

        for _distro in redhat_distro_list:
            if search(pattern=_distro, string=release_content):
                redhat_distro = (
                    _distro.lower()
                    if redhat_distro_list.index(_distro) == 0
                    else _distro[3 : len(_distro) + 1]
                )
                if redhat_distro in ["centos", "rhel"]:
                    redhat_distro = "centos"
                break

    # No need for alpine because "Alpine".lower() == "alpine"
    # The same rule also applies for Solus, Slackware, openwrt
    if distro == "funtoo":
        distro = "gentoo"

    if distro == "opensuse":
        distro = "suse"

    return (
        [distro, debian_distro] if not debian_distro == "" else [distro, redhat_distro]
    )
