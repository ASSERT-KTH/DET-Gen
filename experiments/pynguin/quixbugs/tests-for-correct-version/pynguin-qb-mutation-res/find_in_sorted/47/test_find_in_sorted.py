# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import find_in_sorted as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    str_0 = "; :RhXg8Ts"
    var_0 = module_0.find_in_sorted(str_0, str_0)
    assert var_0 == -1
    var_1 = module_0.find_in_sorted(str_0, str_0)
    assert var_1 == -1
    bool_0 = False
    module_0.find_in_sorted(bool_0, str_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    bytes_0 = b"\xc7\xa6"
    int_0 = -938
    bool_0 = True
    tuple_0 = (bytes_0, int_0, bool_0)
    tuple_1 = (tuple_0,)
    int_1 = -82
    dict_0 = {tuple_1: int_1, int_1: tuple_1, tuple_0: tuple_1, bytes_0: int_0}
    module_0.find_in_sorted(dict_0, dict_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    none_type_0 = None
    module_0.find_in_sorted(none_type_0, none_type_0)


@pytest.mark.xfail(strict=True)
def test_case_3():
    int_0 = -1366
    list_0 = [int_0]
    var_0 = module_0.find_in_sorted(list_0, int_0)
    assert var_0 == 0
    int_1 = 470
    none_type_0 = None
    module_0.find_in_sorted(int_1, none_type_0)