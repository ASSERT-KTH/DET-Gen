# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import is_valid_parenthesization as module_0


def test_case_0():
    bytes_0 = b"\x93\xbaj\x84"
    var_0 = module_0.is_valid_parenthesization(bytes_0)
    assert var_0 is False


def test_case_1():
    list_0 = []
    var_0 = module_0.is_valid_parenthesization(list_0)
    assert var_0 is True


@pytest.mark.xfail(strict=True)
def test_case_2():
    list_0 = []
    bool_0 = True
    tuple_0 = (list_0, bool_0)
    var_0 = module_0.is_valid_parenthesization(list_0)
    assert var_0 is True
    var_1 = module_0.is_valid_parenthesization(tuple_0)
    assert var_1 is False
    str_0 = "(jk #R1oov(UDAI#=M"
    var_2 = module_0.is_valid_parenthesization(str_0)
    assert var_2 is False
    module_0.is_valid_parenthesization(var_2)