# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_2147 as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    module_0.func()


def test_case_1():
    bytes_0 = b"~\xf0\xa0\xc6\xe39I#\x80B\xaf\xe8a0\xa4\xf9\xfa"
    var_0 = module_0.func(*bytes_0)
    assert var_0 == 282863


@pytest.mark.xfail(strict=True)
def test_case_2():
    bytes_0 = b"\x01@\x94\xd0\x0b"
    var_0 = module_0.func(*bytes_0)
    assert var_0 == 1
    module_0.func(*var_0)


@pytest.mark.xfail(strict=True)
def test_case_3():
    bool_0 = False
    str_0 = "w Sch"
    list_0 = [bool_0, bool_0, str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == 1
    var_1 = module_0.func(*list_0)
    assert var_1 == 1
    bytes_0 = b"\x04\xe2\x89u"
    var_2 = module_0.func(*bytes_0)
    assert var_2 == 27
    module_0.func()
