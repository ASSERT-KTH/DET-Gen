# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_2113 as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_1():
    bytes_0 = b"\x95\xc3\xcc\x014\x96p\xfb\xf9K"
    var_0 = module_0.func(*bytes_0)
    assert var_0 == 52
    module_0.func(*var_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    bytes_0 = b"P\x96\xcb!\xfd,>\xe0\x1d"
    var_0 = module_0.func(*bytes_0)
    assert var_0 == 12
    module_0.func(*var_0)
