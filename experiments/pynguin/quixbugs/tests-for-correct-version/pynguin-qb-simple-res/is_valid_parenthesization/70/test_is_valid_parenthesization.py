# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import is_valid_parenthesization as module_0


def test_case_0():
    str_0 = "?m"
    var_0 = module_0.is_valid_parenthesization(str_0)
    assert var_0 is False


def test_case_1():
    str_0 = "?m"
    tuple_0 = ()
    var_0 = module_0.is_valid_parenthesization(tuple_0)
    assert var_0 is True
    var_1 = module_0.is_valid_parenthesization(tuple_0)
    assert var_1 is True
    var_2 = module_0.is_valid_parenthesization(str_0)
    assert var_2 is False
    var_3 = module_0.is_valid_parenthesization(tuple_0)
    assert var_3 is True
    var_4 = module_0.is_valid_parenthesization(tuple_0)
    assert var_4 is True
    var_5 = module_0.is_valid_parenthesization(str_0)
    assert var_5 is False
    var_6 = module_0.is_valid_parenthesization(str_0)
    assert var_6 is False


@pytest.mark.xfail(strict=True)
def test_case_2():
    bool_0 = False
    module_0.is_valid_parenthesization(bool_0)


@pytest.mark.xfail(strict=True)
def test_case_3():
    str_0 = "(l2%q"
    var_0 = module_0.is_valid_parenthesization(str_0)
    assert var_0 is False
    module_0.is_valid_parenthesization(var_0)