from py_apps.utils.sys import get_distro_fullname, get_distro_short_name


def test_distro_name() -> None:
    assert get_distro_short_name() == ["debian", "ubuntu"]
