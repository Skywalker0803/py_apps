"""
A "confirm-only" notice dialog
"""

from textual.app import App, ComposeResult

from textual.widgets import Label


class Notice(App[str]):
    """A "confirm-only" notice dialog"""

    def compose(self) -> ComposeResult:
        yield Label("ss")
