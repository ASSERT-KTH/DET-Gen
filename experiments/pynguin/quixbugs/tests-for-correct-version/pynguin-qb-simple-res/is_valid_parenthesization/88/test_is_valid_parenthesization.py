# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import is_valid_parenthesization as module_0


def test_case_0():
    str_0 = "18+"
    var_0 = module_0.is_valid_parenthesization(str_0)
    assert var_0 is False


@pytest.mark.xfail(strict=True)
def test_case_1():
    set_0 = set()
    var_0 = module_0.is_valid_parenthesization(set_0)
    assert var_0 is True
    none_type_0 = None
    module_0.is_valid_parenthesization(none_type_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    bool_0 = True
    module_0.is_valid_parenthesization(bool_0)


@pytest.mark.xfail(strict=True)
def test_case_3():
    str_0 = "(F,p/B45XC, "
    var_0 = module_0.is_valid_parenthesization(str_0)
    assert var_0 is False
    bytes_0 = b"\xf3\x10fS\x1e}\x81\x9a?\xd6\x85w\xc3G8\x9a\xafb\xd8\x06"
    var_1 = module_0.is_valid_parenthesization(bytes_0)
    assert var_1 is False
    str_1 = ""
    var_2 = module_0.is_valid_parenthesization(str_1)
    assert var_2 is True
    module_0.is_valid_parenthesization(var_2)