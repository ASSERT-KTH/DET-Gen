# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_2593 as module_0
import builtins as module_1


def test_case_0():
    str_0 = "4MrBzb[{L(UuoH"
    var_0 = module_0.func(*str_0)
    assert var_0 == 4


def test_case_1():
    bytes_0 = b"i\x84\x8b.\xd3"
    var_0 = module_0.func(*bytes_0)
    assert var_0 == 99


@pytest.mark.xfail(strict=True)
def test_case_2():
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_3():
    int_0 = 2286
    set_0 = {int_0, int_0, int_0}
    var_0 = module_0.func(*set_0)
    assert var_0 == 1999
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_4():
    bytes_0 = b"\xc4t\x08\xe5"
    var_0 = module_0.func(*bytes_0)
    assert var_0 == 189
    module_0.func(*var_0)


@pytest.mark.xfail(strict=True)
def test_case_5():
    bytes_0 = b"mn\xe3"
    bytes_1 = b"l\xfb\x95"
    var_0 = module_0.func(*bytes_1)
    assert var_0 == 99
    var_1 = module_0.func(*bytes_0)
    assert var_1 == 99
    bool_0 = True
    list_0 = [bool_0, bool_0, bool_0, bool_0]
    object_0 = module_1.object()
    var_2 = module_0.func(*list_0)
    assert var_2 == 1
    module_0.func()
