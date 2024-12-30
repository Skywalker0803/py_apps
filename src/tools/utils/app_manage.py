"""
This module provides some functions for managing sys apps
"""

from os import path
from subprocess import CalledProcessError, run

from .errors import UnknownPkgManagerError

_pkg_dict: dict[str, list[str]] = {
    "debian": ["eatmydata", "apt"],
    "alpine": ["apk"],
    "arch": ["pacman"],
    "centos": ["yum"],
    "fedora": ["yum"],
    "openwrt": ["opkg"],
    "gentoo": ["emerge"],
    "suse": ["dnf"],
    "void": ["xbps-install"],
    "slackware": ["slackpkg"],
}

_install_dict: dict[str, str] = {
    "debian": "install",
    "alpine": "add",
    "arch": "-Sy",
    "centos": "install",
    "fedora": "install",
    "openwrt": "install",
    "gentoo": "-vk",
    "suse": "install",
    "void": "-S",
    "slackware": "install",
}

_update_dict: dict[str, str] = {
    "debian": "update",
    "alpine": "update",
    "centos": "update",
    "fedora": "update",
    "openwrt": "update",
    "suse": "update",
}

_install_opt_dict: dict[str, list[str]] = {
    "debian": ["-y"],
    "centos": ["-y", "--skip-broken"],
    "fedora": ["-y", "--skip-broken"],
    "suse": ["-y", "--skip-broken"],
    "void": ["-y"],
}


def install_app(distro: str, app: str, app_dep: str = "") -> None:
    """
    Install the appointed app and its dependencies for the given distro

    Params:
        distro: the distro given
        app: the app to be installed
        app_dep: the dependencies to be installed, in the form of "a b c"

    Type:
        distro: str
        app: str
        app_dep: str | None

    Throws: UnknownPkgManagerError
    """
    app_dep_list: list[str] = app_dep.split(" ")

    # Declaring pkg manager & installation command & updating command & extra options
    pkg: list[str] | None = _pkg_dict.get(distro, None)
    install: str | None = _install_dict.get(distro, None)
    update: str = _update_dict.get(distro, "")
    extra_options: list[str] = _install_opt_dict.get(distro, [])

    if pkg is None or install is None:
        raise UnknownPkgManagerError(distro=distro)

    if pkg[0] in ["fedora", "centos"] and path.exists("/usr/bin/dnf"):
        pkg = ["dnf"]

    # For debian & ubuntu
    if distro in ["debian", "ubuntu"]:
        extra_options = ["-y"]
    # For archlinux
    elif distro == "arch":
        extra_options = ["--noconfirm", "--needed"]
    # For redhat
    elif distro in ["centos", "fedora"]:
        extra_options = ["-y", "--skip-broken"]
    # For suse
    elif distro == "suse":
        extra_options = ["-y", "--skip-broken"]
        if path.exists("/usr/bin/zypper"):
            pkg = ["zypper"]
            install = "in"
            update = ""
            extra_options.pop()
    # For void linux
    elif distro == "void":
        extra_options = ["-y"]

    try:
        # If there is an updating command, update
        if not update == "":
            run(args=[*pkg, update], check=True)
        # Execute sudo [pkg] [install] [app] [dependencies] [options]
        run(["sudo", *pkg, install, app, *app_dep_list, *extra_options], check=True)
    except CalledProcessError as e:
        print(f"\033[91m\033[1m[Error]\033[0m Error when installing {app} {app_dep}")
        print(f"\033[31mError message\033[0m\n\t{e.output}")
