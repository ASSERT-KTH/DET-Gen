# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_2170 as module_0
import builtins as module_1


def test_case_0():
    float_0 = 548.9
    int_0 = -341
    list_0 = [float_0, float_0, int_0, float_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == 207885


@pytest.mark.xfail(strict=True)
def test_case_1():
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_2():
    bool_0 = False
    dict_0 = {bool_0: bool_0, bool_0: bool_0, bool_0: bool_0, bool_0: bool_0}
    list_0 = [bool_0, bool_0, dict_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == 1
    module_1.object(*list_0)
