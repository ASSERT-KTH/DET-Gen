# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import is_valid_parenthesization as module_0
import builtins as module_1


def test_case_0():
    str_0 = "'K-W\t;y+"
    var_0 = module_0.is_valid_parenthesization(str_0)
    assert var_0 is False


@pytest.mark.xfail(strict=True)
def test_case_1():
    int_0 = 380
    module_0.is_valid_parenthesization(int_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    list_0 = []
    var_0 = module_0.is_valid_parenthesization(list_0)
    assert var_0 is True
    var_1 = module_0.is_valid_parenthesization(list_0)
    assert var_1 is True
    var_2 = module_0.is_valid_parenthesization(list_0)
    assert var_2 is True
    var_3 = module_0.is_valid_parenthesization(list_0)
    assert var_3 is True
    none_type_0 = None
    module_0.is_valid_parenthesization(none_type_0)


@pytest.mark.xfail(strict=True)
def test_case_3():
    str_0 = "("
    var_0 = module_0.is_valid_parenthesization(str_0)
    assert var_0 is False
    str_1 = "'K-W\t;y+"
    var_1 = module_0.is_valid_parenthesization(str_1)
    assert var_1 is False
    module_1.object(**var_1)


@pytest.mark.xfail(strict=True)
def test_case_4():
    str_0 = "(4"
    var_0 = module_0.is_valid_parenthesization(str_0)
    assert var_0 is True
    str_1 = "'K-W\t;y+"
    var_1 = module_0.is_valid_parenthesization(str_1)
    assert var_1 is False
    module_0.is_valid_parenthesization(var_0)