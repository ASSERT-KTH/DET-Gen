# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_104 as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    bool_0 = True
    int_0 = 1345
    bool_1 = True
    bool_2 = False
    tuple_0 = (int_0, bool_1, bool_2)
    list_0 = [bool_0, bool_0, tuple_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == "a"
    module_0.func()


def test_case_1():
    float_0 = -1903.12
    list_0 = [float_0, float_0, float_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == ""
    list_1 = [float_0, float_0, float_0, var_0]
    var_1 = module_0.func(*list_1)
    assert var_1 == ""
    list_2 = [float_0, var_1, var_1]
    var_2 = module_0.func(*list_2)
    assert var_2 == ""


@pytest.mark.xfail(strict=True)
def test_case_2():
    module_0.func()
