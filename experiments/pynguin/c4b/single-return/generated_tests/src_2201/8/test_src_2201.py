# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_2201 as module_0


def test_case_0():
    float_0 = 1365.2411
    list_0 = [float_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == 15


@pytest.mark.xfail(strict=True)
def test_case_1():
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_2():
    bool_0 = True
    list_0 = [bool_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == 1
    module_0.func(*var_0)
