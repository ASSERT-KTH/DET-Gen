# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_1895 as module_0


def test_case_0():
    int_0 = 1961
    tuple_0 = (int_0,)
    list_0 = [tuple_0, tuple_0, tuple_0, tuple_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == 1


@pytest.mark.xfail(strict=True)
def test_case_1():
    bytes_0 = b""
    list_0 = [bytes_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == 0
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_2():
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_3():
    bool_0 = True
    tuple_0 = (bool_0, bool_0)
    list_0 = [tuple_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == 3
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_4():
    bool_0 = True
    bool_1 = False
    tuple_0 = (bool_0, bool_1)
    list_0 = [tuple_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == 2
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_5():
    float_0 = -4015.4
    list_0 = [float_0]
    bool_0 = False
    list_1 = [list_0, list_0, bool_0, bool_0]
    module_0.func(*list_1)
