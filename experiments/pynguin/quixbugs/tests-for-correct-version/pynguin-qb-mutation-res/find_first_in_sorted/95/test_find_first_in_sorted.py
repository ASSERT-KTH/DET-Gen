# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import find_first_in_sorted as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    bytes_0 = b"\xb0\xed\x1c \xcf\xc9bl\xa1V|\xda\xda\x9f\x8eac"
    module_0.find_first_in_sorted(bytes_0, bytes_0)


def test_case_1():
    tuple_0 = ()
    bool_0 = True
    var_0 = module_0.find_first_in_sorted(tuple_0, bool_0)
    assert var_0 == -1
    var_1 = module_0.find_first_in_sorted(tuple_0, bool_0)
    assert var_1 == -1


@pytest.mark.xfail(strict=True)
def test_case_2():
    none_type_0 = None
    module_0.find_first_in_sorted(none_type_0, none_type_0)


@pytest.mark.xfail(strict=True)
def test_case_3():
    str_0 = "u"
    var_0 = module_0.find_first_in_sorted(str_0, str_0)
    assert var_0 == 0
    module_0.find_first_in_sorted(var_0, str_0)


@pytest.mark.xfail(strict=True)
def test_case_4():
    str_0 = "u"
    var_0 = module_0.find_first_in_sorted(str_0, str_0)
    assert var_0 == 0
    tuple_0 = (str_0,)
    bytes_0 = b"T\x92\xca"
    var_1 = module_0.find_first_in_sorted(bytes_0, var_0)
    assert var_1 == -1
    tuple_1 = (var_0, tuple_0, tuple_0, tuple_0)
    module_0.find_first_in_sorted(tuple_1, var_0)


@pytest.mark.xfail(strict=True)
def test_case_5():
    str_0 = "v\\h"
    var_0 = module_0.find_first_in_sorted(str_0, str_0)
    assert var_0 == -1
    module_0.find_first_in_sorted(var_0, str_0)


@pytest.mark.xfail(strict=True)
def test_case_6():
    complex_0 = 408.872963 - 1427.464561j
    list_0 = [complex_0, complex_0]
    module_0.find_first_in_sorted(list_0, complex_0)


@pytest.mark.xfail(strict=True)
def test_case_7():
    str_0 = "u"
    var_0 = module_0.find_first_in_sorted(str_0, str_0)
    assert var_0 == 0
    bool_0 = True
    tuple_0 = (str_0, bool_0)
    var_1 = module_0.find_first_in_sorted(tuple_0, bool_0)
    assert var_1 == 1
    module_0.find_first_in_sorted(var_0, var_0)