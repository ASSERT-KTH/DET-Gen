# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import is_valid_parenthesization as module_0
import builtins as module_1


def test_case_0():
    str_0 = "uI5oeS|"
    var_0 = module_0.is_valid_parenthesization(str_0)
    assert var_0 is False


@pytest.mark.xfail(strict=True)
def test_case_1():
    var_0 = module_1.object()
    list_0 = []
    var_1 = module_0.is_valid_parenthesization(list_0)
    assert var_1 is True
    bool_0 = False
    module_0.is_valid_parenthesization(bool_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    none_type_0 = None
    module_0.is_valid_parenthesization(none_type_0)


def test_case_3():
    bytes_0 = b"\xec:\x1dsfL\x0f\xe1KB5\xe5u\xb5\x0cM`rb!"
    str_0 = "("
    set_0 = {bytes_0, bytes_0, str_0, str_0}
    var_0 = module_0.is_valid_parenthesization(bytes_0)
    assert var_0 is False
    var_1 = module_0.is_valid_parenthesization(set_0)
    assert var_1 is True
    var_2 = module_0.is_valid_parenthesization(set_0)
    assert var_2 is True
    var_3 = module_0.is_valid_parenthesization(bytes_0)
    assert var_3 is False
    var_4 = module_0.is_valid_parenthesization(bytes_0)
    assert var_4 is False
    var_5 = module_0.is_valid_parenthesization(bytes_0)
    assert var_5 is False