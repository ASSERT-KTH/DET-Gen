# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_1895 as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    module_0.func()


def test_case_1():
    bytes_0 = b"\x03\x00"
    list_0 = [bytes_0, bytes_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == 3


@pytest.mark.xfail(strict=True)
def test_case_2():
    bool_0 = True
    list_0 = [bool_0, bool_0, bool_0]
    list_1 = [list_0, list_0]
    var_0 = module_0.func(*list_1)
    assert var_0 == 7
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_3():
    bool_0 = False
    list_0 = [bool_0, bool_0, bool_0]
    list_1 = [list_0, list_0]
    var_0 = module_0.func(*list_1)
    assert var_0 == 0
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_4():
    int_0 = -310
    list_0 = [int_0, int_0, int_0]
    list_1 = [list_0, int_0, int_0, list_0]
    module_0.func(*list_1)
