# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_2217 as module_0


def test_case_0():
    bool_0 = True
    list_0 = [bool_0, bool_0, bool_0, bool_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == "NO"


@pytest.mark.xfail(strict=True)
def test_case_1():
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_2():
    bytes_0 = b"M\xc6\xa9M\x92"
    var_0 = module_0.func(*bytes_0)
    assert var_0 == "YES"
    var_1 = module_0.func(*bytes_0)
    assert var_1 == "YES"
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_3():
    bytes_0 = b"\x14\xad\xbb\xc7\xa2>\x13\xafh\xef7"
    var_0 = module_0.func(*bytes_0)
    assert var_0 == "YES"
    module_0.func(*var_0)


@pytest.mark.xfail(strict=True)
def test_case_4():
    bytes_0 = b"/\xbau\xd2\xec\xbbw\xb4:\x1b\x06S\xe7uBP\xf1\xed"
    var_0 = module_0.func(*bytes_0)
    assert var_0 == "YES"
    module_0.func(*var_0)
