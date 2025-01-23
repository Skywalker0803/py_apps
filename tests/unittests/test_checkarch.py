from py3_tmoe.utils.sys import check_architecture


def test_checkarch():
    assert check_architecture() == "arm64"
