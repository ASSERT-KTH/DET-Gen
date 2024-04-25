# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import levenshtein as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    str_0 = '{^".Q!\x0b@j9{8'
    var_0 = module_0.levenshtein(str_0, str_0)
    assert var_0 == 0
    module_0.levenshtein(var_0, var_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    float_0 = -85.4535
    module_0.levenshtein(float_0, float_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    str_0 = "B?]"
    bytes_0 = b"\xbe,6\xb17\xa8\x06\xbd\x05\xa6b\x84>"
    module_0.levenshtein(str_0, bytes_0)


@pytest.mark.xfail(strict=True)
def test_case_3():
    str_0 = "Y"
    list_0 = [str_0, str_0, str_0]
    var_0 = module_0.levenshtein(list_0, str_0)
    assert var_0 == 2
    var_1 = module_0.levenshtein(str_0, str_0)
    assert var_1 == 0
    var_2 = module_0.levenshtein(str_0, list_0)
    assert var_2 == 2
    none_type_0 = None
    var_3 = module_0.levenshtein(list_0, str_0)
    assert var_3 == 2
    module_0.levenshtein(var_3, none_type_0)