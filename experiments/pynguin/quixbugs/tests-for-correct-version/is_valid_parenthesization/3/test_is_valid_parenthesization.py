# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import is_valid_parenthesization as module_0


def test_case_0():
    str_0 = "mY'W('"
    bool_0 = True
    list_0 = [str_0, str_0, bool_0, str_0]
    var_0 = module_0.is_valid_parenthesization(list_0)
    assert var_0 is False


def test_case_1():
    set_0 = set()
    var_0 = module_0.is_valid_parenthesization(set_0)
    assert var_0 is True


@pytest.mark.xfail(strict=True)
def test_case_2():
    float_0 = -124.35
    module_0.is_valid_parenthesization(float_0)


@pytest.mark.xfail(strict=True)
def test_case_3():
    str_0 = "(2F"
    var_0 = module_0.is_valid_parenthesization(str_0)
    assert var_0 is False
    module_0.is_valid_parenthesization(var_0)
