# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import find_in_sorted as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    list_0 = []
    var_0 = module_0.find_in_sorted(list_0, list_0)
    assert var_0 == -1
    none_type_0 = None
    module_0.find_in_sorted(none_type_0, var_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    bytes_0 = b'\t"\x05U\x8a\x0c/\x0b\xa0(\xa2\x94\x8cR'
    none_type_0 = None
    module_0.find_in_sorted(bytes_0, none_type_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    none_type_0 = None
    module_0.find_in_sorted(none_type_0, none_type_0)


@pytest.mark.xfail(strict=True)
def test_case_3():
    str_0 = "%*B4BNE)db"
    var_0 = module_0.find_in_sorted(str_0, str_0)
    assert var_0 == -1
    var_1 = module_0.find_in_sorted(str_0, str_0)
    assert var_1 == -1
    module_0.find_in_sorted(var_0, var_1)


@pytest.mark.xfail(strict=True)
def test_case_4():
    str_0 = "\x0bM=k\r+J#DW_*cr@"
    list_0 = [str_0, str_0, str_0]
    tuple_0 = (list_0, str_0)
    var_0 = module_0.find_in_sorted(tuple_0, str_0)
    assert var_0 == 1
    float_0 = -664.0
    module_0.find_in_sorted(float_0, float_0)