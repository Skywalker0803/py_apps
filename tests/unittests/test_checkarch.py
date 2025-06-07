from py_apps.utils.sys import check_architecture


def test_checkarch():
    assert check_architecture() == "arm64"
