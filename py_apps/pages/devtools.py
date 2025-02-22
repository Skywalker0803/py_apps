"""Run DevTools selection page"""

from py_apps.apps.devtools.jetbrains import Jetbrains, JetbrainsVariants
from py_apps.apps.devtools.neovim import Neovim, NvimVariants
from py_apps.apps.devtools.vscode import VSCode as VSCode
from py_apps.ui.selection import Selection as Selection


def run() -> bool:
    """Run DevTools selection page"""

    selection = Selection(
        idlist=["vscode", "nvim", *[e.value for e in JetbrainsVariants], "back"],
        itemlist=[
            "Visual Studio Code：微软出品，宇宙第一编辑器",
            "Neovim 加配置：极致的效率，极客们的最爱",
            *[
                {
                    "idea_professional": "IntelliJ IDEA Ultimate Edition：适用于 Java Web 开发",
                    "idea_community": "IntelliJ IDEA Community Edition：阉割版 Java & Kotlin IDE（免费）",
                    "python_professional": "PyCharm Professional Edition：极其强大的数据科学和 Web 开发用 IDE",
                    "python_community": "PyCharm Community Edition：纯 Python 开发必备（免费）",
                    "go": "GoLand：为 Gophers 打造的完美 IDE",
                    "webide": "PhpStorm：为 PHP 开发人员赋能",
                    "webstorm": "WebStorm：JavaScript & TypeScript 的 IDE（非商业使用免费）",
                    "cpp": "CLion：开发 C / C++ ，化繁为简，驾驭力量",
                    "rider": "Rider：全世界最受欢迎的 .NET & C# 游戏开发 IDE（非商业使用免费）",
                    "ruby": "RubyMine：Ruby on Rails 的 all-in-one 解决方案",
                    "rustrover": "RustRover：智能 Rust IDE（非商业使用免费）",
                }[e.value]
                for e in JetbrainsVariants
            ],
            "返回上级菜单",
        ],
        dialog_title="工欲善其事，必先利其器：请选择称手的开发工具",
    ).run()

    # Deciding block: decide which installer to use
    match selection:
        case "vscode":
            VSCode().prepare().install()

        case "nvim":
            variant = Selection(
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

        case val if val in [e.value for e in JetbrainsVariants]:
            print(val)
            Jetbrains(
                JetbrainsVariants(JetbrainsVariants._value2member_map_[val])
            ).prepare().install()

        # In-page loop logic: True to go back and False to continue
        case _:
            return True

    return False


def devtools():
    """Devtools page looping func"""

    # Inter-page loop logic: return to go back
    while True:
        if run():
            return
