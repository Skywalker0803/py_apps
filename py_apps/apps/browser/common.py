"""Some common things for browser classes"""

from typing import Any


class Browser:
    """Defines a type for chain methods"""

    def __init__(self) -> None:
        pass

    def prepare(self) -> Any:
        """Prepare method for overwrite"""
        return self

    def install(self) -> Any:
        """Install method for overwrite"""
        return self
