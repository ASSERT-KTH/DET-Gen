# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import find_in_sorted as module_0
import builtins as module_1


def test_case_0():
    int_0 = -252
    tuple_0 = (int_0,)
    float_0 = 1596.0
    tuple_1 = (tuple_0, float_0, int_0)
    bool_0 = True
    dict_0 = {tuple_0: tuple_0, tuple_0: int_0, float_0: bool_0, tuple_0: int_0}
    tuple_2 = (int_0, tuple_1, dict_0, dict_0)
    tuple_3 = (tuple_2, int_0)
    int_1 = 2323
    var_0 = module_0.find_in_sorted(tuple_3, int_1)
    assert var_0 == -1


@pytest.mark.xfail(strict=True)
def test_case_1():
    str_0 = "4Z/8iPlKxJ,F-"
    none_type_0 = None
    module_0.find_in_sorted(str_0, none_type_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    none_type_0 = None
    module_0.find_in_sorted(none_type_0, none_type_0)


@pytest.mark.xfail(strict=True)
def test_case_3():
    str_0 = "&Avo1u- \tf"
    var_0 = module_0.find_in_sorted(str_0, str_0)
    assert var_0 == -1
    bool_0 = False
    module_0.find_in_sorted(bool_0, bool_0)


@pytest.mark.xfail(strict=True)
def test_case_4():
    bool_0 = False
    list_0 = [bool_0, bool_0, bool_0, bool_0]
    var_0 = module_0.find_in_sorted(list_0, bool_0)
    assert var_0 == 2
    module_1.object(*var_0, **var_0)