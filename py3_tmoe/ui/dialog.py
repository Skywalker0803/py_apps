"""
This module contains the non-scrollable dialog screen
"""

from typing import Any

from textual.app import App, ComposeResult
from textual.widgets import Button, Label


class Dialog(App[str]):
    """
    Horizontal non-scrollable selection dialog

    Params:
        list[str] idlist: list of id for returning the selected item
        list[str] itemlist: item list, support Console Markup
        str dialog_title: the title of the dialog
    """

    CSS_PATH = "dialog.tcss"

    def __init__(
        self,
        idlist: list[str],
        itemlist: list[str],
        dialog_title: str = "",
    ):
        super().__init__()

        # Declare the id list, list of items & title
        self.idlist = idlist
        self.itemlist = itemlist
        self.title = dialog_title

        # Setup button list for manipulating the button's width
        self.buttonlist: list[Button] = []

    def compose(self) -> ComposeResult:
        """
        Compose method, which composes the widgets
        """
        yield Label(self.title)  # Render the title of the dialog

        # Iterate the item list
        for item in self.itemlist:
            button_variant: Any = "default"  # Set the default theme as "default"

            # Check the content of button
            # the buttom will be green if the content is "Yes"
            if item in ["确认", "Yes"]:
                button_variant = "success"
            # The button will be red if the content is "Cancel"
            elif item in ["取消", "Cancel"]:
                button_variant = "error"
            # The button will be blue if the content is "Back"
            elif item in ["返回", "Back"]:
                button_variant = "primary"

            button: Button = Button(
                item,
                id=self.idlist[self.itemlist.index(item)],
                variant=button_variant,
            )
            # Add the button into the list for changing width of it later
            self.buttonlist.append(button)
            yield button  # Rendering the button

    def on_mount(self) -> None:
        """
        Setup the grid amount when the screen is mounted
        """
        # The stylesheet is 2 by default, the grid is 12 * 2 by default
        # Set the width to 4 if the count of buttons is 3
        if len(self.idlist) == 3:
            for button in self.buttonlist:
                button.styles.column_span = 4
        # Set the width to 3 if the count of buttons is 4
        elif len(self.idlist) == 4:
            for button in self.buttonlist:
                button.styles.column_span = 3

    def on_button_pressed(self, event: Button.Pressed):
        """
        Process the on press event for returning it
        """
        self.exit(event.button.id)  # Return the selected id of the button
