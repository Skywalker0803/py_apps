"""
This module contains some common vars for utils
"""

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

distro_aliases: dict[str, str] = {
    # No need for alpine because "Alpine".lower() == "alpine"
    # The same rule also applies for Solus, Slackware, openwrt
    # ------- Aliases -------
    # For debian based sys
    "debian": "debian",
    "ubuntu": "debian",
    "Kali": "debian",
    "deepin": "debian",
    "uos.com": "debian",
    # For redhat based sys
    "fedora": "redhat",
    "centos": "redhat",
    "redhat": "redhat",
    # For arch based sys
    "manjaro": "arch",
    # For gentoo
    "funtoo": "gentoo",
    # For SUSE
    "openSUSE": "suse",
}

architecture_aliases: dict[str, str] = {
    "armv7*": "armhf",
    "armv8l": "armhf",
    "armv[1-6]*": "armel",
    "aarch64": "arm64",
    "armv8*": "arm64",
    "arm64": "arm64",
    "arm*": "arm64",
    "x86_64": "amd64",
    "amd64": "amd64",
    "i*86": "i386",
    "x86": "i386",
    "s390*": "s390x",
    "ppc*": "ppc64el",
    "mips64": "mips64el",
    "mips*": "mipsel",
    "risc*": "riscv64",
}
