# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_452 as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_1():
    int_0 = -3421
    list_0 = [int_0, int_0]
    var_0 = module_0.func(*list_0)
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_2():
    bool_0 = True
    list_0 = [bool_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == 1
    int_0 = -3421
    list_1 = [int_0, int_0]
    var_1 = module_0.func(*list_1)
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_3():
    int_0 = 2990
    list_0 = [int_0, int_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == 1
    module_0.func(*var_0)
