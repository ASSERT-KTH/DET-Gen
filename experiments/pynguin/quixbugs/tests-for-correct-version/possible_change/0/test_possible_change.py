# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import possible_change as module_0


def test_case_0():
    bool_0 = False
    var_0 = module_0.possible_change(bool_0, bool_0)
    assert var_0 == 1
    var_1 = module_0.possible_change(var_0, bool_0)
    assert var_1 == 1


def test_case_1():
    bool_0 = True
    tuple_0 = (bool_0,)
    var_0 = module_0.possible_change(tuple_0, bool_0)
    assert var_0 == 1


@pytest.mark.xfail(strict=True)
def test_case_2():
    float_0 = -971.7
    var_0 = module_0.possible_change(float_0, float_0)
    assert var_0 == 0
    bool_0 = True
    none_type_0 = None
    module_0.possible_change(bool_0, none_type_0)
