# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import possible_change as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    bool_0 = False
    var_0 = module_0.possible_change(bool_0, bool_0)
    assert var_0 == 1
    str_0 = "u|k7z\r>C1p"
    var_1 = module_0.possible_change(str_0, bool_0)
    assert var_1 == 1
    module_0.possible_change(str_0, var_1)


@pytest.mark.xfail(strict=True)
def test_case_1():
    bool_0 = True
    module_0.possible_change(bool_0, bool_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    float_0 = -2216.0
    dict_0 = {float_0: float_0, float_0: float_0, float_0: float_0, float_0: float_0}
    var_0 = module_0.possible_change(dict_0, float_0)
    assert var_0 == 0
    var_1 = module_0.possible_change(var_0, float_0)
    assert var_1 == 0
    bool_0 = False
    none_type_0 = None
    module_0.possible_change(bool_0, none_type_0)


@pytest.mark.xfail(strict=True)
def test_case_3():
    int_0 = 1734
    dict_0 = {int_0: int_0}
    var_0 = module_0.possible_change(dict_0, int_0)
    assert var_0 == 1
    none_type_0 = None
    module_0.possible_change(none_type_0, none_type_0)