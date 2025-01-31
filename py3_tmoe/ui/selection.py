"""
This module contains the scrollable list dialog screen
"""

from textual.app import App, ComposeResult
from textual.containers import Center, Container, VerticalScroll
from textual.widgets import Button, Label


class Selection(App[str]):
    """
    Vertical scrollable list screen

    Params:
        idlist: the id of list item, for getting the selected item id
        itemlist: content list, supports Console Markup
        dialogTitle: the title of dialog

    Type:
        idlist: List[str]
        itemlist: List[str]
        dialog_title: str
    """

    CSS_PATH = "selection.tcss"

    def __init__(
        self,
        idlist: list[str],
        itemlist: list[str],
        dialog_title: str,
    ):
        super().__init__()

        # Declare id list & item list & title of the dialog
        self.idlist = idlist
        self.itemlist = itemlist
        self.title = dialog_title

    def compose(self) -> ComposeResult:
        """
        Compose method, composing the widgets together
        """
        # Setup the button list for rendering
        buttonlist: list[Button] = []

        # Iterate the item list
        for item in self.itemlist:
            button: Button = Button(
                item,
                id=self.idlist[self.itemlist.index(item)],
            )
            buttonlist.append(button)  # Append the button to the button list

        # Add the margin for title and list only
        yield Container(
            Center(Label(self.title), id="title"),
            VerticalScroll(*buttonlist),
            id="container",
        )
        # Tips on using method
        yield Label(":bulb:[b]小提示：[/b]用Tab键选择，回车键按下，或使用触摸屏点击")

    def on_button_pressed(self, event: Button.Pressed):
        """
        Process on press event for the buttons
        """
        self.exit(event.button.id)  # Return the item id which is selected on exit
