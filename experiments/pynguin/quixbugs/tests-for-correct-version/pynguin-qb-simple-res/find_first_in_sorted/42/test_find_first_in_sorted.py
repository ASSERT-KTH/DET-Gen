# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import find_first_in_sorted as module_0
import builtins as module_1


def test_case_0():
    str_0 = "h"
    var_0 = module_0.find_first_in_sorted(str_0, str_0)
    assert var_0 == 0


@pytest.mark.xfail(strict=True)
def test_case_1():
    tuple_0 = ()
    var_0 = module_0.find_first_in_sorted(tuple_0, tuple_0)
    assert var_0 == -1
    complex_0 = 1343.68407 - 3696.83j
    module_0.find_first_in_sorted(complex_0, var_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    none_type_0 = None
    module_0.find_first_in_sorted(none_type_0, none_type_0)


@pytest.mark.xfail(strict=True)
def test_case_3():
    str_0 = "bi>cQj[5C+:STH$,uw"
    var_0 = module_0.find_first_in_sorted(str_0, str_0)
    assert var_0 == -1
    object_0 = module_1.object()
    module_0.find_first_in_sorted(object_0, str_0)


@pytest.mark.xfail(strict=True)
def test_case_4():
    bytes_0 = b"i\xf7\xf4\x8b\x88\x93\x9eO\xb9j|,C"
    list_0 = [bytes_0, bytes_0, bytes_0, bytes_0, bytes_0, bytes_0]
    bool_0 = False
    tuple_0 = (bytes_0, list_0, list_0, bool_0)
    var_0 = module_0.find_first_in_sorted(list_0, bytes_0)
    assert var_0 == 0
    module_0.find_first_in_sorted(tuple_0, var_0)


@pytest.mark.xfail(strict=True)
def test_case_5():
    bytes_0 = b"i\xf7\xf4\x8b\x88\x93\x9eO\xb9j|,C"
    list_0 = [bytes_0, bytes_0, bytes_0, bytes_0]
    bool_0 = False
    tuple_0 = (bytes_0, list_0, list_0, bool_0)
    var_0 = module_0.find_first_in_sorted(tuple_0, list_0)
    assert var_0 == 1
    bytes_1 = b"\xca\xd1O\x88"
    module_0.find_first_in_sorted(bytes_1, bytes_1)