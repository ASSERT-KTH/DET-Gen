# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import bitcount as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    float_0 = 4636.6112
    module_0.bitcount(float_0)


def test_case_1():
    dict_0 = {}
    var_0 = module_0.bitcount(dict_0)
    assert var_0 == 0


@pytest.mark.xfail(strict=True)
def test_case_2():
    int_0 = -311
    module_0.bitcount(int_0)


def test_case_3():
    int_0 = 2977
    none_type_0 = None
    var_0 = module_0.bitcount(none_type_0)
    assert var_0 == 0
    var_1 = module_0.bitcount(none_type_0)
    assert var_1 == 0
    var_2 = module_0.bitcount(int_0)
    assert var_2 == 6
    set_0 = set()
    var_3 = module_0.bitcount(var_0)
    assert var_3 == 0
    var_4 = module_0.bitcount(set_0)
    assert var_4 == 0