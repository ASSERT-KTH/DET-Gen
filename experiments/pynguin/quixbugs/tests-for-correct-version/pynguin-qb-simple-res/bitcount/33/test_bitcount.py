# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import bitcount as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    int_0 = -145
    module_0.bitcount(int_0)


def test_case_1():
    none_type_0 = None
    var_0 = module_0.bitcount(none_type_0)
    assert var_0 == 0
    none_type_1 = None
    var_1 = module_0.bitcount(none_type_1)
    assert var_1 == 0


def test_case_2():
    bool_0 = True
    none_type_0 = None
    var_0 = module_0.bitcount(bool_0)
    assert var_0 == 1
    var_1 = module_0.bitcount(none_type_0)
    assert var_1 == 0
    var_2 = module_0.bitcount(bool_0)
    assert var_2 == 1
    var_3 = module_0.bitcount(bool_0)
    assert var_3 == 1
    var_4 = module_0.bitcount(none_type_0)
    assert var_4 == 0
    var_5 = module_0.bitcount(none_type_0)
    assert var_5 == 0
    var_6 = module_0.bitcount(var_2)
    assert var_6 == 1