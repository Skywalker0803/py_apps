"""
Other utils in this proj
"""

from os import path
from re import sub
from subprocess import check_output

from py_apps.utils.app_manage import install_app


def to_snakecase(string: str):
    """
    Params:
        str string: the input string
    """

    return "_".join(
        sub(
            "([A-Z][a-z]+)", r" \1", sub("([A-Z]+)", r" \1", string.replace("-", " "))
        ).split()
    ).lower()


def fix_electron_libxssl(distro: str) -> None:
    """Fix electron libxssl problem"""
    match distro:
        case "debian":
            if not check_output(["whereis", "libnss3.so"]) == "libnss3.so:":
                install_app(distro, ["libnss3"])
        case "redhat":
            install_app(distro, ["libXScrnSaver"])
        case "arch":
            if not path.exists("/usr/lib/libnss3.so"):
                install_app(distro, ["nss"])
        case "suse":
            install_app(distro, ["mozilla-nss"])
        case _:
            install_app(distro, ["nss"])
