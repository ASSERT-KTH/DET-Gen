# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import bitcount as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    bool_0 = False
    none_type_0 = None
    var_0 = module_0.bitcount(none_type_0)
    assert var_0 == 0
    str_0 = "#tc!(c"
    tuple_0 = (bool_0, str_0, str_0)
    module_0.bitcount(tuple_0)


def test_case_1():
    bool_0 = False
    var_0 = module_0.bitcount(bool_0)
    assert var_0 == 0


def test_case_2():
    int_0 = 2731
    var_0 = module_0.bitcount(int_0)
    assert var_0 == 7
    var_1 = module_0.bitcount(var_0)
    assert var_1 == 3
    var_2 = module_0.bitcount(int_0)
    assert var_2 == 7
    var_3 = module_0.bitcount(var_0)
    assert var_3 == 3
    var_4 = module_0.bitcount(var_0)
    assert var_4 == 3
    var_5 = module_0.bitcount(var_2)
    assert var_5 == 3