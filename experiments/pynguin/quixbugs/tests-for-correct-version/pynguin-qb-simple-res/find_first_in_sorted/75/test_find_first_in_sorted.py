# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import find_first_in_sorted as module_0


def test_case_0():
    str_0 = "d5Iv"
    var_0 = module_0.find_first_in_sorted(str_0, str_0)
    assert var_0 == -1


@pytest.mark.xfail(strict=True)
def test_case_1():
    tuple_0 = ()
    var_0 = module_0.find_first_in_sorted(tuple_0, tuple_0)
    assert var_0 == -1
    float_0 = -1361.7
    bool_0 = False
    var_1 = module_0.find_first_in_sorted(tuple_0, bool_0)
    assert var_1 == -1
    module_0.find_first_in_sorted(float_0, bool_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    none_type_0 = None
    module_0.find_first_in_sorted(none_type_0, none_type_0)


@pytest.mark.xfail(strict=True)
def test_case_3():
    str_0 = "d5Iv"
    list_0 = [str_0, str_0]
    var_0 = module_0.find_first_in_sorted(list_0, str_0)
    assert var_0 == 0
    module_0.find_first_in_sorted(str_0, list_0)


@pytest.mark.xfail(strict=True)
def test_case_4():
    str_0 = "!\rPB@Y"
    var_0 = module_0.find_first_in_sorted(str_0, str_0)
    assert var_0 == -1
    list_0 = [var_0, str_0, var_0, var_0]
    var_1 = module_0.find_first_in_sorted(list_0, var_0)
    assert var_1 == 2
    module_0.find_first_in_sorted(var_0, list_0)