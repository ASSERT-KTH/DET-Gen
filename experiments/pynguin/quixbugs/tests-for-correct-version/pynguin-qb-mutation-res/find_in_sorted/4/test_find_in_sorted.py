# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import find_in_sorted as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    tuple_0 = ()
    var_0 = module_0.find_in_sorted(tuple_0, tuple_0)
    assert var_0 == -1
    bytes_0 = b"5y\xe1\x943\x9c1\xf0\x96\xa5B\x05 \x93\xf3\x81\xb8(\x80\xc3"
    none_type_0 = None
    module_0.find_in_sorted(bytes_0, none_type_0)


def test_case_1():
    bytes_0 = b"\xbb\x9dWA'\xd1j\xd542\xd2_\x9e"
    bool_0 = True
    tuple_0 = (bytes_0, bool_0)
    var_0 = module_0.find_in_sorted(tuple_0, bool_0)
    assert var_0 == 1


@pytest.mark.xfail(strict=True)
def test_case_2():
    bool_0 = False
    module_0.find_in_sorted(bool_0, bool_0)


@pytest.mark.xfail(strict=True)
def test_case_3():
    tuple_0 = ()
    var_0 = module_0.find_in_sorted(tuple_0, tuple_0)
    assert var_0 == -1
    bytes_0 = b"5y\xe1\x943\x9c1\xf0\x96\xa5B\x05 \x93\xf3\x81\xb8(\x80\xc3"
    list_0 = module_0.find_in_sorted(bytes_0, var_0)
    assert list_0 == -1
    none_type_0 = None
    module_0.find_in_sorted(bytes_0, none_type_0)


@pytest.mark.xfail(strict=True)
def test_case_4():
    str_0 = "yH)B>|4"
    var_0 = module_0.find_in_sorted(str_0, str_0)
    assert var_0 == -1
    var_1 = module_0.find_in_sorted(str_0, str_0)
    assert var_1 == -1
    module_0.find_in_sorted(var_0, var_1)