# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_381 as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    bool_0 = True
    list_0 = [bool_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == "1"
    var_1 = module_0.func(*list_0)
    assert var_1 == "1"
    var_2 = module_0.func(*var_1)
    assert var_2 == "1"
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_1():
    int_0 = 2293
    set_0 = {int_0, int_0, int_0}
    list_0 = [int_0, set_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == "8"
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_2():
    int_0 = -2311
    list_0 = [int_0, int_0]
    module_0.func(*list_0)


@pytest.mark.xfail(strict=True)
def test_case_3():
    module_0.func()
