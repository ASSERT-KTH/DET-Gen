# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import find_first_in_sorted as module_0
import builtins as module_1


def test_case_0():
    str_0 = "[nwydCm$\n[L3"
    var_0 = module_0.find_first_in_sorted(str_0, str_0)
    assert var_0 == -1


@pytest.mark.xfail(strict=True)
def test_case_1():
    dict_0 = {}
    var_0 = module_0.find_first_in_sorted(dict_0, dict_0)
    assert var_0 == -1
    module_0.find_first_in_sorted(var_0, var_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    int_0 = -516
    module_0.find_first_in_sorted(int_0, int_0)


@pytest.mark.xfail(strict=True)
def test_case_3():
    str_0 = "o"
    var_0 = module_0.find_first_in_sorted(str_0, str_0)
    assert var_0 == 0
    none_type_0 = None
    module_0.find_first_in_sorted(none_type_0, none_type_0)


@pytest.mark.xfail(strict=True)
def test_case_4():
    str_0 = "AI.aj$1"
    var_0 = module_0.find_first_in_sorted(str_0, str_0)
    assert var_0 == -1
    none_type_0 = None
    tuple_0 = (var_0, var_0, var_0)
    var_1 = module_0.find_first_in_sorted(tuple_0, var_0)
    assert var_1 == 0
    list_0 = [none_type_0]
    module_1.object(*list_0, **var_0)


@pytest.mark.xfail(strict=True)
def test_case_5():
    str_0 = "AI.aj$1"
    var_0 = module_0.find_first_in_sorted(str_0, str_0)
    assert var_0 == -1
    none_type_0 = None
    tuple_0 = (none_type_0, var_0, var_0)
    tuple_1 = (var_0,)
    var_1 = module_0.find_first_in_sorted(tuple_1, var_0)
    assert var_1 == 0
    var_2 = module_0.find_first_in_sorted(tuple_0, var_0)
    assert var_2 == 1
    list_0 = [var_2]
    module_1.object(*list_0, **var_0)