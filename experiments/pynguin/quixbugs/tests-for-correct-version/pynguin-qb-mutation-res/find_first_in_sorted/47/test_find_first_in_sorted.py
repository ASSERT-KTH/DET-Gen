# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import find_first_in_sorted as module_0
import builtins as module_1


def test_case_0():
    str_0 = "z/qO\\\nm3t'#"
    var_0 = module_0.find_first_in_sorted(str_0, str_0)
    assert var_0 == -1


@pytest.mark.xfail(strict=True)
def test_case_1():
    tuple_0 = ()
    var_0 = module_0.find_first_in_sorted(tuple_0, tuple_0)
    assert var_0 == -1
    var_1 = module_0.find_first_in_sorted(tuple_0, var_0)
    assert var_1 == -1
    var_2 = module_0.find_first_in_sorted(tuple_0, tuple_0)
    assert var_2 == -1
    var_3 = module_0.find_first_in_sorted(tuple_0, tuple_0)
    assert var_3 == -1
    var_4 = module_0.find_first_in_sorted(tuple_0, var_2)
    assert var_4 == -1
    var_5 = module_0.find_first_in_sorted(tuple_0, tuple_0)
    assert var_5 == -1
    none_type_0 = None
    var_6 = module_0.find_first_in_sorted(tuple_0, none_type_0)
    assert var_6 == -1
    var_7 = module_0.find_first_in_sorted(tuple_0, tuple_0)
    assert var_7 == -1
    module_0.find_first_in_sorted(var_2, none_type_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    int_0 = -2079
    bool_0 = True
    tuple_0 = (int_0, int_0, int_0, bool_0)
    var_0 = module_0.find_first_in_sorted(tuple_0, bool_0)
    assert var_0 == 3
    var_1 = module_0.find_first_in_sorted(tuple_0, var_0)
    assert var_1 == -1
    var_2 = module_0.find_first_in_sorted(tuple_0, int_0)
    assert var_2 == 0
    module_0.find_first_in_sorted(var_1, var_0)


def test_case_3():
    int_0 = -2079
    bool_0 = True
    tuple_0 = (int_0, int_0, int_0, bool_0)
    var_0 = module_0.find_first_in_sorted(tuple_0, bool_0)
    assert var_0 == 3
    object_0 = module_1.object()