# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import possible_change as module_0


def test_case_0():
    bool_0 = True
    bool_1 = False
    var_0 = module_0.possible_change(bool_0, bool_1)
    assert var_0 == 1
    set_0 = {var_0, bool_0, bool_0}
    var_1 = module_0.possible_change(set_0, var_0)
    assert var_1 == 1
    dict_0 = {var_1: var_1, bool_0: bool_1, var_1: bool_0, var_0: bool_1}
    var_2 = module_0.possible_change(dict_0, var_1)
    assert var_2 == 1


@pytest.mark.xfail(strict=True)
def test_case_1():
    none_type_0 = None
    module_0.possible_change(none_type_0, none_type_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    float_0 = -744.3
    var_0 = module_0.possible_change(float_0, float_0)
    assert var_0 == 0
    var_1 = module_0.possible_change(float_0, float_0)
    assert var_1 == 0
    set_0 = {float_0}
    var_2 = module_0.possible_change(var_1, var_1)
    assert var_2 == 1
    module_0.possible_change(set_0, var_2)