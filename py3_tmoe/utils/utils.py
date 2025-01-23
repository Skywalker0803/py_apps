"""
Other utils in this proj
"""

from re import sub


def to_snakecase(string: str) -> str:
    """
    Change the given string to the from of a_b_c (Snake Case)

    Params:
        str string: the input string
    """

    return "_".join(
        sub(
            "([A-Z][a-z]+)", r" \1", sub("([A-Z]+)", r" \1", string.replace("-", " "))
        ).split()
    ).lower()
