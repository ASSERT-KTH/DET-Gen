# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_1035 as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    bool_0 = False
    list_0 = [bool_0, bool_0, bool_0, bool_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == 1
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_1():
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_2():
    bool_0 = True
    list_0 = [bool_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == 5
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_3():
    float_0 = 4716.0
    list_0 = [float_0, float_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == 25
    bool_0 = False
    list_1 = [bool_0, bool_0, bool_0, bool_0]
    var_1 = module_0.func(*list_1)
    assert var_1 == 1
    module_0.func()
