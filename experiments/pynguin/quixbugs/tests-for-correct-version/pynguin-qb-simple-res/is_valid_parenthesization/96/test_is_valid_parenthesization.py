# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import is_valid_parenthesization as module_0


def test_case_0():
    str_0 = "@=}BT\t"
    var_0 = module_0.is_valid_parenthesization(str_0)
    assert var_0 is False


@pytest.mark.xfail(strict=True)
def test_case_1():
    str_0 = ""
    dict_0 = {str_0: str_0, str_0: str_0, str_0: str_0, str_0: str_0}
    var_0 = module_0.is_valid_parenthesization(dict_0)
    assert var_0 is False
    var_1 = module_0.is_valid_parenthesization(str_0)
    assert var_1 is True
    none_type_0 = None
    module_0.is_valid_parenthesization(none_type_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    str_0 = "("
    var_0 = module_0.is_valid_parenthesization(str_0)
    assert var_0 is False
    complex_0 = -485.591 + 253j
    module_0.is_valid_parenthesization(complex_0)


@pytest.mark.xfail(strict=True)
def test_case_3():
    bytes_0 = b"\xf0_\x80GEf\x0fg\x98J\xf7\xb8\x87\xd07r#JQ\xa1"
    var_0 = module_0.is_valid_parenthesization(bytes_0)
    assert var_0 is False
    var_1 = module_0.is_valid_parenthesization(bytes_0)
    assert var_1 is False
    str_0 = "(XfQeUUl'\"~>xw="
    var_2 = module_0.is_valid_parenthesization(str_0)
    assert var_2 is False
    var_3 = module_0.is_valid_parenthesization(bytes_0)
    assert var_3 is False
    module_0.is_valid_parenthesization(var_1)