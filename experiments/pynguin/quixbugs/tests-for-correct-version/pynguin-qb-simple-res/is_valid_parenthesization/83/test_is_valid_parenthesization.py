# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import is_valid_parenthesization as module_0
import builtins as module_1


def test_case_0():
    bytes_0 = b"3\x94H\x02P\xbb@\x85\xf57\xd6wD\xd1%\xfa3"
    list_0 = [bytes_0, bytes_0, bytes_0, bytes_0]
    var_0 = module_0.is_valid_parenthesization(list_0)
    assert var_0 is False


@pytest.mark.xfail(strict=True)
def test_case_1():
    bool_0 = False
    module_0.is_valid_parenthesization(bool_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    str_0 = 'Ad{"iW^R!\\9.AH'
    var_0 = module_0.is_valid_parenthesization(str_0)
    assert var_0 is False
    dict_0 = {}
    var_1 = module_0.is_valid_parenthesization(dict_0)
    assert var_1 is True
    module_0.is_valid_parenthesization(var_1)


@pytest.mark.xfail(strict=True)
def test_case_3():
    object_0 = module_1.object()
    str_0 = "(:A,\x0cl{>GR@FZ"
    var_0 = module_0.is_valid_parenthesization(str_0)
    assert var_0 is False
    module_0.is_valid_parenthesization(object_0)