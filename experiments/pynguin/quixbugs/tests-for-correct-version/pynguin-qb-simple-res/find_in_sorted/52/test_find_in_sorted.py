# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import find_in_sorted as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    list_0 = []
    bytes_0 = b"\x08\xb8\xe2\x92x\xa9\xf65"
    var_0 = module_0.find_in_sorted(list_0, bytes_0)
    assert var_0 == -1
    module_0.find_in_sorted(bytes_0, list_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    str_0 = "jw"
    none_type_0 = None
    module_0.find_in_sorted(str_0, none_type_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    none_type_0 = None
    module_0.find_in_sorted(none_type_0, none_type_0)


@pytest.mark.xfail(strict=True)
def test_case_3():
    tuple_0 = ()
    none_type_0 = None
    var_0 = module_0.find_in_sorted(tuple_0, none_type_0)
    assert var_0 == -1
    str_0 = "jw"
    var_1 = module_0.find_in_sorted(str_0, str_0)
    assert var_1 == -1
    none_type_1 = None
    module_0.find_in_sorted(str_0, none_type_1)


@pytest.mark.xfail(strict=True)
def test_case_4():
    float_0 = 615.0
    list_0 = [float_0, float_0, float_0, float_0]
    var_0 = module_0.find_in_sorted(list_0, float_0)
    assert var_0 == 2
    module_0.find_in_sorted(float_0, list_0)