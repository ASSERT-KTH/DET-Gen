# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import possible_change as module_0


def test_case_0():
    int_0 = -395
    var_0 = module_0.possible_change(int_0, int_0)
    assert var_0 == 0
    var_1 = module_0.possible_change(var_0, int_0)
    assert var_1 == 0
    var_2 = module_0.possible_change(var_0, var_0)
    assert var_2 == 1
    var_3 = module_0.possible_change(int_0, int_0)
    assert var_3 == 0


@pytest.mark.xfail(strict=True)
def test_case_1():
    none_type_0 = None
    module_0.possible_change(none_type_0, none_type_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    int_0 = 3196
    list_0 = [int_0, int_0, int_0, int_0]
    complex_0 = -135.1 - 660.94j
    tuple_0 = (list_0, list_0, complex_0)
    module_0.possible_change(tuple_0, int_0)


def test_case_3():
    int_0 = 2012
    set_0 = {int_0, int_0}
    var_0 = module_0.possible_change(set_0, int_0)
    assert var_0 == 1