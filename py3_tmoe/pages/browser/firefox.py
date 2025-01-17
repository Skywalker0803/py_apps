from py3_tmoe.apps.browser.firefox import FirefoxVariants, Firefox
from py3_tmoe.ui.dialog import Dialog


def install_for_esr() -> None:
    firefox_instance = Firefox(FirefoxVariants.ESR)
    firefox_instance.prepare()
    firefox_instance.install()


def install_for_firefox() -> None:
    firefox_instance = Firefox(FirefoxVariants.FIREFOX)
    firefox_instance.prepare()
    firefox_instance.install()


def firefox_or_esr() -> None:
    dialog = Dialog(
        idlist=["firefox", "esr"],
        itemlist=["Firefox 火狐浏览器", "Firefox ESR 长期支持版"],
        dialogTitle="Firefox 还是 ESR ？",
    )

    result = dialog.run()
    match result:
        case "firefox":
            install_for_firefox()

        case "esr":
            install_for_esr()
