# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import possible_change as module_0


def test_case_0():
    float_0 = -3354.24239
    var_0 = module_0.possible_change(float_0, float_0)
    assert var_0 == 0
    var_1 = module_0.possible_change(float_0, var_0)
    assert var_1 == 1
    var_2 = module_0.possible_change(float_0, var_0)
    assert var_2 == 1
    var_3 = module_0.possible_change(float_0, float_0)
    assert var_3 == 0
    var_4 = module_0.possible_change(var_2, var_0)
    assert var_4 == 1


@pytest.mark.xfail(strict=True)
def test_case_1():
    int_0 = 306
    module_0.possible_change(int_0, int_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    bool_0 = False
    var_0 = module_0.possible_change(bool_0, bool_0)
    assert var_0 == 1
    var_1 = module_0.possible_change(bool_0, var_0)
    assert var_1 == 0
    tuple_0 = (var_1, var_1)
    module_0.possible_change(var_1, tuple_0)