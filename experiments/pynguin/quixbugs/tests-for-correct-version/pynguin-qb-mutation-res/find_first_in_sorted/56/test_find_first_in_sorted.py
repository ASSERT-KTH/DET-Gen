# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import find_first_in_sorted as module_0
import builtins as module_1


def test_case_0():
    bool_0 = False
    list_0 = [bool_0, bool_0, bool_0, bool_0]
    var_0 = module_0.find_first_in_sorted(list_0, bool_0)
    assert var_0 == 0


@pytest.mark.xfail(strict=True)
def test_case_1():
    set_0 = set()
    var_0 = module_0.find_first_in_sorted(set_0, set_0)
    assert var_0 == -1
    var_1 = module_0.find_first_in_sorted(set_0, set_0)
    assert var_1 == -1
    module_0.find_first_in_sorted(var_1, var_1)


@pytest.mark.xfail(strict=True)
def test_case_2():
    object_0 = module_1.object()
    module_0.find_first_in_sorted(object_0, object_0)


@pytest.mark.xfail(strict=True)
def test_case_3():
    str_0 = ",)ob`y3?Oq-0aG6b7_"
    var_0 = module_0.find_first_in_sorted(str_0, str_0)
    assert var_0 == -1
    module_0.find_first_in_sorted(var_0, str_0)


@pytest.mark.xfail(strict=True)
def test_case_4():
    int_0 = 928
    list_0 = [int_0, int_0]
    var_0 = module_0.find_first_in_sorted(list_0, int_0)
    assert var_0 == 0
    str_0 = "`"
    list_1 = [str_0, list_0, str_0, var_0]
    var_1 = module_0.find_first_in_sorted(list_1, str_0)
    assert var_1 == 2
    var_2 = module_0.find_first_in_sorted(str_0, str_0)
    assert var_2 == 0
    bytes_0 = b"Z8Md(\x02\x8f"
    module_0.find_first_in_sorted(str_0, bytes_0)