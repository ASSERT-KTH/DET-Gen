# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_38 as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    float_0 = 943.151565
    set_0 = {float_0, float_0, float_0, float_0}
    list_0 = [float_0, set_0, set_0]
    var_0 = module_0.func(*list_0)
    list_1 = [float_0, float_0, float_0, float_0]
    var_1 = module_0.func(*list_1)
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_1():
    bool_0 = True
    list_0 = [bool_0, bool_0, bool_0, bool_0]
    var_0 = module_0.func(*list_0)
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_2():
    module_0.func()