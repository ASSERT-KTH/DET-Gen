# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_1613 as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    int_0 = 1351
    list_0 = [int_0, int_0, int_0, int_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == 360
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_1():
    bool_0 = False
    list_0 = [bool_0, bool_0, bool_0, bool_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == 0
    int_0 = -486
    list_1 = [int_0, int_0, int_0]
    var_1 = module_0.func(*list_1)
    assert var_1 == 0
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_2():
    module_0.func()
