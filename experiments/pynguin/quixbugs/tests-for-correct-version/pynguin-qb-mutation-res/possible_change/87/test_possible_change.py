# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import possible_change as module_0


def test_case_0():
    bool_0 = False
    set_0 = {bool_0, bool_0, bool_0}
    var_0 = module_0.possible_change(set_0, bool_0)
    assert var_0 == 1


@pytest.mark.xfail(strict=True)
def test_case_1():
    tuple_0 = ()
    module_0.possible_change(tuple_0, tuple_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    float_0 = -3035.964
    var_0 = module_0.possible_change(float_0, float_0)
    assert var_0 == 0
    int_0 = 1246
    module_0.possible_change(int_0, int_0)


@pytest.mark.xfail(strict=True)
def test_case_3():
    bool_0 = True
    none_type_0 = None
    var_0 = module_0.possible_change(none_type_0, bool_0)
    assert var_0 == 0
    module_0.possible_change(bool_0, none_type_0)