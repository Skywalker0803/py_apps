from py_apps.apps.devtools.neovim import Neovim, NvimVariants
from py_apps.apps.devtools.vscode import VSCode as _VSCode
from py_apps.ui.selection import Selection as _Selection


def run() -> None:
    """Run DevTools selection page"""
    selection = _Selection(
        idlist=["vscode", "nvim"],
        itemlist=[
            "Visual Studio Code：微软出品，宇宙第一编辑器",
            "Neovim 加配置：极致的效率，极客们的最爱",
        ],
        dialog_title="工欲善其事，必先利其器：请选择称手的开发工具",
    ).run()

    match selection:
        case "vscode":
            _VSCode().prepare().install()

        case "nvim":
            variant = _Selection(
                idlist=["default", "astro", "space", "lazy", "lunar", "nvchad"],
                itemlist=[
                    "默认（无配置）",
                    "AstroNvim：Configure less, code more",
                    "SpaceVim：一个模块化的 Vim 和 Neovim 配置集合",
                    "LazyVim：Lazy.nvim 包管理器作者出品，配置简单，懒人专属",
                    "LunarVim：开箱即用的 Neovim IDE 层",
                    "NvChad：拥有高度可定制的 UI，默认易用",
                ],
                dialog_title="Neovim：您想要什么配置文件呢？",
            ).run()
            Neovim(NvimVariants(variant)).prepare().install()
        case _:
            exit("TODO")
