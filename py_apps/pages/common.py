"""Some common utils for pages"""

from types import FunctionType


def loop(page: FunctionType):
    """Page loop function"""

    # Inter-page loop logic: return to go back
    while True:
        if page():
            return
