# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import is_valid_parenthesization as module_0


def test_case_0():
    str_0 = "L+`?8mbK6w3Q|pUe"
    var_0 = module_0.is_valid_parenthesization(str_0)
    assert var_0 is False


def test_case_1():
    str_0 = "(h"
    var_0 = module_0.is_valid_parenthesization(str_0)
    assert var_0 is True