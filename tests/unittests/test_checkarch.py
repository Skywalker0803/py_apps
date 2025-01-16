from py3_tmoe.utils.utils import check_architecture


def test_checkarch():
    assert check_architecture() == "arm64"
