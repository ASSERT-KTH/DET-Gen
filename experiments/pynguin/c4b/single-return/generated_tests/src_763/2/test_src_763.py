# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_763 as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    bool_0 = False
    dict_0 = {bool_0: bool_0, bool_0: bool_0}
    list_0 = [bool_0, dict_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == 1
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_1():
    float_0 = -550.7378
    list_0 = [float_0, float_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == 565692443
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_2():
    module_0.func()
