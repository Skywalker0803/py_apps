from py3_tmoe.utils.cmd import check_cmd_exists


def test_check_if_cmd_exists():
    assert check_cmd_exists("aria2c")
    assert check_cmd_exists("fish") is False
