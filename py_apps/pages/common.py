"""Some common utils for pages"""

from typing import Callable


def loop(page: Callable):
    """Page loop function"""

    # Inter-page loop logic: return to go back
    while True:
        if page():
            return
