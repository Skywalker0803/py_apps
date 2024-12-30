"""
This module contains some basic util functions
"""

from csv import reader
from re import sub


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

    with open("/etc/os-release", encoding="utf-8") as f:
        release_reader = reader(f, delimiter="=")
        for row in release_reader:
            if row:
                release_data[row[0]] = row[1]

        if release_data["ID"] in ["debian", "raspbian"]:
            with open("/etc/debian_version", encoding="utf-8") as f:
                debian_version = f.readline().strip()
                major_version = debian_version.split(".")[0]
            version_split = release_data["VERSION"].split(" ", maxsplit=1)
            if version_split[0] == major_version:
                # Just major version shown, replace it with the full version
                release_data["VERSION"] = " ".join([debian_version] + version_split[1:])

        return f"{release_data['NAME']} {release_data['VERSION']}"


def get_distro_short_name() -> str:
    """
    Get the shortened version of current Linux distro name (such as ubuntu, debian)
    """
    return to_snakecase(get_distro_fullname()).split("_", maxsplit=1)[0]
