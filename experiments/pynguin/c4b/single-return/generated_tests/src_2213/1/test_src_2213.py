# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_2213 as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    float_0 = -359.888369
    list_0 = [float_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == -358
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_1():
    int_0 = 1315
    list_0 = [int_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == 1320
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_2():
    module_0.func()
