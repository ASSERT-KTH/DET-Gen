# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import bitcount as module_0
import builtins as module_1


@pytest.mark.xfail(strict=True)
def test_case_0():
    none_type_0 = None
    var_0 = module_0.bitcount(none_type_0)
    assert var_0 == 0
    var_1 = module_0.bitcount(var_0)
    assert var_1 == 0
    list_0 = [var_0, none_type_0, var_0, var_0]
    tuple_0 = (var_0, list_0)
    list_1 = [tuple_0, list_0, none_type_0, none_type_0]
    module_0.bitcount(list_1)


@pytest.mark.xfail(strict=True)
def test_case_1():
    none_type_0 = None
    module_1.object(**none_type_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    int_0 = -3004
    module_0.bitcount(int_0)


@pytest.mark.xfail(strict=True)
def test_case_3():
    none_type_0 = None
    var_0 = module_0.bitcount(none_type_0)
    assert var_0 == 0
    none_type_1 = None
    var_1 = module_0.bitcount(none_type_1)
    assert var_1 == 0
    bool_0 = True
    none_type_2 = None
    var_2 = module_0.bitcount(none_type_2)
    assert var_2 == 0
    var_3 = module_0.bitcount(bool_0)
    assert var_3 == 1
    int_0 = -531
    var_4 = module_0.bitcount(bool_0)
    assert var_4 == 1
    var_5 = module_0.bitcount(bool_0)
    assert var_5 == 1
    module_0.bitcount(int_0)