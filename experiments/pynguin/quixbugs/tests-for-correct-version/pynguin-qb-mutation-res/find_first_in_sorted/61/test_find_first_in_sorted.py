# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import find_first_in_sorted as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    bytes_0 = b"\n7Q\x10\x84"
    module_0.find_first_in_sorted(bytes_0, bytes_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    set_0 = set()
    var_0 = module_0.find_first_in_sorted(set_0, set_0)
    assert var_0 == -1
    none_type_0 = None
    module_0.find_first_in_sorted(var_0, none_type_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    int_0 = -695
    module_0.find_first_in_sorted(int_0, int_0)


@pytest.mark.xfail(strict=True)
def test_case_3():
    bool_0 = True
    list_0 = [bool_0]
    var_0 = module_0.find_first_in_sorted(list_0, bool_0)
    assert var_0 == 0
    bytes_0 = b"\xc4\x06\xf3"
    module_0.find_first_in_sorted(bytes_0, bytes_0)


def test_case_4():
    bytes_0 = b'\xc4"\x06\xf3'
    float_0 = -269.0
    var_0 = module_0.find_first_in_sorted(bytes_0, float_0)
    assert var_0 == -1


@pytest.mark.xfail(strict=True)
def test_case_5():
    str_0 = "Np3\n"
    var_0 = module_0.find_first_in_sorted(str_0, str_0)
    assert var_0 == -1
    var_1 = module_0.find_first_in_sorted(str_0, str_0)
    assert var_1 == -1
    module_0.find_first_in_sorted(str_0, var_1)


def test_case_6():
    bool_0 = True
    list_0 = [bool_0, bool_0]
    var_0 = module_0.find_first_in_sorted(list_0, bool_0)
    assert var_0 == 0


@pytest.mark.xfail(strict=True)
def test_case_7():
    int_0 = -833
    dict_0 = {int_0: int_0, int_0: int_0}
    str_0 = "> vi6\ndh_"
    tuple_0 = ()
    tuple_1 = (int_0, dict_0, str_0, tuple_0)
    var_0 = module_0.find_first_in_sorted(tuple_1, str_0)
    assert var_0 == 2
    bool_0 = True
    module_0.find_first_in_sorted(bool_0, bool_0)