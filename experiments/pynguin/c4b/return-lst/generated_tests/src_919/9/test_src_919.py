# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_919 as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_1():
    float_0 = 2260.4729619475283
    int_0 = -3331
    list_0 = [float_0, int_0]
    var_0 = module_0.func(*list_0)
    var_1 = module_0.func(*var_0)
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_2():
    bool_0 = True
    int_0 = 1398
    list_0 = [bool_0, bool_0, int_0, int_0]
    var_0 = module_0.func(*list_0)
    float_0 = 2247.702839
    int_1 = -3343
    list_1 = [float_0, int_1]
    var_1 = module_0.func(*list_1)
    var_2 = module_0.func(*var_1)
    module_0.func()
