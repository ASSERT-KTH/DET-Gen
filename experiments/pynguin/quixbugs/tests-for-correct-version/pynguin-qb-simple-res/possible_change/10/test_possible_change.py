# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import possible_change as module_0


def test_case_0():
    bool_0 = False
    var_0 = module_0.possible_change(bool_0, bool_0)
    assert var_0 == 1


@pytest.mark.xfail(strict=True)
def test_case_1():
    none_type_0 = None
    module_0.possible_change(none_type_0, none_type_0)


def test_case_2():
    float_0 = -22.0
    var_0 = module_0.possible_change(float_0, float_0)
    assert var_0 == 0
    var_1 = module_0.possible_change(float_0, float_0)
    assert var_1 == 0
    var_2 = module_0.possible_change(float_0, float_0)
    assert var_2 == 0
    var_3 = module_0.possible_change(var_0, var_0)
    assert var_3 == 1
    var_4 = module_0.possible_change(var_3, float_0)
    assert var_4 == 0
    set_0 = set()
    bool_0 = True
    var_5 = module_0.possible_change(set_0, bool_0)
    assert var_5 == 0


@pytest.mark.xfail(strict=True)
def test_case_3():
    none_type_0 = None
    bool_0 = True
    var_0 = module_0.possible_change(none_type_0, bool_0)
    assert var_0 == 0
    module_0.possible_change(none_type_0, none_type_0)


@pytest.mark.xfail(strict=True)
def test_case_4():
    bool_0 = True
    module_0.possible_change(bool_0, bool_0)