# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import lis as module_0


def test_case_0():
    bool_0 = False
    dict_0 = {bool_0: bool_0, bool_0: bool_0, bool_0: bool_0}
    var_0 = module_0.lis(dict_0)
    assert var_0 == 1


def test_case_1():
    tuple_0 = ()
    var_0 = module_0.lis(tuple_0)
    assert var_0 == 0


@pytest.mark.xfail(strict=True)
def test_case_2():
    str_0 = "LRND>L1lEMvQzjo\t"
    var_0 = module_0.lis(str_0)
    assert var_0 == 6
    set_0 = {var_0, var_0}
    int_0 = -2539
    tuple_0 = (set_0, int_0, var_0)
    module_0.lis(tuple_0)


@pytest.mark.xfail(strict=True)
def test_case_3():
    none_type_0 = None
    module_0.lis(none_type_0)


@pytest.mark.xfail(strict=True)
def test_case_4():
    str_0 = "00PUD5!_8L3"
    var_0 = module_0.lis(str_0)
    assert var_0 == 4
    var_1 = module_0.lis(str_0)
    assert var_1 == 4
    var_2 = module_0.lis(str_0)
    assert var_2 == 4
    module_0.lis(var_2)