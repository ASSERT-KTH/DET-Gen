# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import find_first_in_sorted as module_0


def test_case_0():
    int_0 = -485
    tuple_0 = (int_0,)
    var_0 = module_0.find_first_in_sorted(tuple_0, int_0)
    assert var_0 == 0


@pytest.mark.xfail(strict=True)
def test_case_1():
    dict_0 = {}
    var_0 = module_0.find_first_in_sorted(dict_0, dict_0)
    assert var_0 == -1
    module_0.find_first_in_sorted(var_0, var_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    none_type_0 = None
    module_0.find_first_in_sorted(none_type_0, none_type_0)


@pytest.mark.xfail(strict=True)
def test_case_3():
    int_0 = -485
    tuple_0 = (int_0,)
    var_0 = module_0.find_first_in_sorted(tuple_0, int_0)
    assert var_0 == 0
    module_0.find_first_in_sorted(tuple_0, tuple_0)


@pytest.mark.xfail(strict=True)
def test_case_4():
    bool_0 = True
    list_0 = [bool_0, bool_0]
    var_0 = module_0.find_first_in_sorted(list_0, bool_0)
    assert var_0 == 0
    module_0.find_first_in_sorted(bool_0, var_0)


@pytest.mark.xfail(strict=True)
def test_case_5():
    bool_0 = True
    list_0 = [bool_0, bool_0]
    var_0 = module_0.find_first_in_sorted(list_0, bool_0)
    assert var_0 == 0
    int_0 = -3310
    bytes_0 = b"\xffK\xaf\xe5u!"
    var_1 = module_0.find_first_in_sorted(bytes_0, int_0)
    assert var_1 == -1
    none_type_0 = None
    module_0.find_first_in_sorted(int_0, none_type_0)


@pytest.mark.xfail(strict=True)
def test_case_6():
    str_0 = "%N|>Vz\\>M_\x0ce%\x0b"
    var_0 = module_0.find_first_in_sorted(str_0, str_0)
    assert var_0 == -1
    module_0.find_first_in_sorted(var_0, var_0)


@pytest.mark.xfail(strict=True)
def test_case_7():
    str_0 = "uqh v7*n,;%\x0c\r]0"
    dict_0 = {str_0: str_0}
    list_0 = []
    int_0 = -1048
    tuple_0 = (str_0, dict_0, list_0, int_0)
    var_0 = module_0.find_first_in_sorted(tuple_0, list_0)
    assert var_0 == 2
    bool_0 = True
    module_0.find_first_in_sorted(bool_0, bool_0)