# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_2213 as module_0


def test_case_0():
    bool_0 = True
    list_0 = [bool_0, bool_0, bool_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == 2


@pytest.mark.xfail(strict=True)
def test_case_1():
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_2():
    int_0 = -519
    list_0 = [int_0, int_0, int_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == -518
    bool_0 = False
    list_1 = [bool_0, bool_0, bool_0]
    var_1 = module_0.func(*list_1)
    assert var_1 == 1
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_3():
    float_0 = 1652.859
    list_0 = [float_0, float_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == 1653
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_4():
    float_0 = 1667.6223035588946
    list_0 = [float_0, float_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == 1670
    module_0.func()