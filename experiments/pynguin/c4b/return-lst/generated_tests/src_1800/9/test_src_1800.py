# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_1800 as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    float_0 = 477.494
    list_0 = [float_0, float_0, float_0, float_0]
    var_0 = module_0.func(*list_0)
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_1():
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_2():
    float_0 = -851.9
    bool_0 = True
    tuple_0 = (bool_0, float_0)
    var_0 = module_0.func(*tuple_0)
    list_0 = [float_0, float_0, float_0]
    var_1 = module_0.func(*list_0)
    module_0.func()
