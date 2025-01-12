from py3_tmoe.tools.utils.utils import check_architecture


def test_checkarch():
    assert check_architecture() == "arm64"
