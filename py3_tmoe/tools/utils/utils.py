"""
This module contains some basic util functions
"""

from csv import reader
from os import path, environ
from pathlib import Path
from platform import machine
from re import search, sub
from subprocess import CalledProcessError
from subprocess import run as process_run

from .common import architecture_aliases, distro_aliases, distro_list


def to_snakecase(string: str) -> str:
    """
    Change the given string to the from of a_b_c (Snake Case)

    Params:
        str string: the input string
    """

    return "_".join(
        sub(
            "([A-Z][a-z]+)", r" \1", sub("([A-Z]+)", r" \1", string.replace("-", " "))
        ).split()
    ).lower()


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


def run(cmd_args: list[str], msg: str = ""):
    """
    The function which runs the command with error processing abilities

    Params:
        list[str] cmd_args: the command list arguments
        str msg: the message printed when an error occurred, usually started with a "when"
    """
    try:
        process_run(args=cmd_args, check=True)
    except CalledProcessError as err:
        print(
            "\033[91m\033[1m[Error]",
            "An error occurred!" if msg == "" else f"An error occurred {msg}",
        )
        print(f"\033[31mError message\033[0m\n\t{err.output}")


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


def check_cmd_exists(cmd: str) -> bool:
    bool_value: int = 0

    for path_item in environ["PATH"].split(":"):
        bool_value += int(path.exists(f"{path_item}/{cmd}"))
    return bool(bool_value)
