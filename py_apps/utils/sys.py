"""
This module contains some basic sys level funcs
"""

from csv import reader
from platform import machine
from re import search

from .common import architecture_aliases, distro_aliases, distro_list


def get_distro_fullname() -> str:
    """
    Get the full name of current Linux distro (such as Ubuntu 22.04.5 LTS (Jammy Jellyfish))

    Returns: str
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


def get_distro_short_name() -> list[str]:
    """
    Get the shortened version of current Linux distro name (such as ubuntu, debian)

    Returns: str
    """

    release_content: str = ""
    with open("/etc/os-release", "r", encoding="utf-8") as release:
        release_content = " ".join(release.readlines())

    distro: str = ""
    debian_distro: str = ""
    redhat_distro: str = ""
    for _distro in distro_list:
        if search(pattern=_distro, string=release_content):
            distro = _distro.replace(" ", "").lower()
            break

    # If the distro is preconfigured as an alias, return its "true" name
    distro = distro_aliases.get(distro, distro)

    debian_distro_list: list[str] = ["ubuntu", "Kali", "deepin", "uos.com"]
    for _distro in debian_distro_list:
        if search(pattern=_distro, string=release_content):
            debian_distro = _distro
            if debian_distro in ["deepin", "uos.com"]:
                debian_distro = "deepin"
            break

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

    return (
        [distro, debian_distro] if not debian_distro == "" else [distro, redhat_distro]
    )


def check_architecture() -> str:
    """
    The function which returns the current architecture

    Returns: str
    """

    machine_type: str = machine().lower()

    architecture: str = ""

    for alias, arch in architecture_aliases.items():
        if search(alias, machine_type):
            architecture = arch
            break

    return architecture
