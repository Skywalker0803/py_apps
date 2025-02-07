"""
Neovim config & setup class
"""

from enum import Enum, unique


@unique
class NvimVariants(Enum):
    """Neovim different configs"""

    LAZY = "lazy"
    LUNAR = "lunar"
    ASTRO = "astro"
    SPACE = "space"
    NVCHAD = "nvchad"
    DEFAULT = "default"
