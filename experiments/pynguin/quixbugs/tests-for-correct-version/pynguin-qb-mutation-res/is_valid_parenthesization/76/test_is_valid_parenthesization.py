# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import is_valid_parenthesization as module_0


def test_case_0():
    str_0 = "qIN)_!\n"
    var_0 = module_0.is_valid_parenthesization(str_0)
    assert var_0 is False


def test_case_1():
    tuple_0 = ()
    var_0 = module_0.is_valid_parenthesization(tuple_0)
    assert var_0 is True
    str_0 = "("
    var_1 = module_0.is_valid_parenthesization(str_0)
    assert var_1 is False


def test_case_2():
    tuple_0 = ()
    var_0 = module_0.is_valid_parenthesization(tuple_0)
    assert var_0 is True
    str_0 = "(h"
    var_1 = module_0.is_valid_parenthesization(str_0)
    assert var_1 is True
    var_2 = module_0.is_valid_parenthesization(tuple_0)
    assert var_2 is True