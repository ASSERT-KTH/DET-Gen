# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_1168 as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    bool_0 = True
    list_0 = [bool_0, bool_0, bool_0, bool_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == 0
    var_1 = module_0.func(*list_0)
    assert var_1 == 0
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_1():
    bool_0 = False
    list_0 = [bool_0, bool_0, bool_0, bool_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == 0
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_2():
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_3():
    bytes_0 = b"\x19g\x87"
    var_0 = module_0.func(*bytes_0)
    assert var_0 == 175
    list_0 = [var_0, var_0, var_0, var_0]
    var_1 = module_0.func(*list_0)
    assert var_1 == 301
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_4():
    int_0 = 677
    int_1 = -3142
    list_0 = [int_0, int_1, int_1]
    var_0 = module_0.func(*list_0)
    assert var_0 == -10997
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_5():
    bytes_0 = b"-X\xed2\\\xa1\xf5?\x91\x16\xe8u\x9a\x99\x19"
    var_0 = module_0.func(*bytes_0)
    assert var_0 == 308
    module_0.func()
