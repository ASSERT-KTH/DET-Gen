# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_2054 as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    float_0 = 2414.56
    set_0 = set()
    list_0 = [float_0, float_0, set_0, set_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == 1999
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_1():
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_2():
    float_0 = 2390.0873496412546
    set_0 = set()
    list_0 = [float_0, float_0, set_0, set_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == 1999
    module_0.func()
