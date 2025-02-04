from py3_tmoe.apps.devtools.vscode import VSCode as _VSCode
from py3_tmoe.ui.selection import Selection as _Selection


def run() -> None:
    """Run DevTools selection page"""
    selection = _Selection(
        idlist=["vscode"],
        itemlist=["Visual Studio Code：微软出品，宇宙第一编辑器"],
        dialog_title="工欲善其事，必先利其器：请选择称手的开发工具",
    ).run()

    match selection:
        case "vscode":
            _VSCode().prepare().install()

        case _:
            exit("TODO")
