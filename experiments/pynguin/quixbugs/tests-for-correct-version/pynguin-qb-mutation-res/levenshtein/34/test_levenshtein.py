# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import levenshtein as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    str_0 = "\r/\x0bb"
    var_0 = module_0.levenshtein(str_0, str_0)
    assert var_0 == 0
    var_1 = module_0.levenshtein(str_0, str_0)
    assert var_1 == 0
    module_0.levenshtein(var_0, var_1)


@pytest.mark.xfail(strict=True)
def test_case_1():
    dict_0 = {}
    module_0.levenshtein(dict_0, dict_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    set_0 = set()
    bytes_0 = b"^\xc3\x8a9\x1eq(\xd8\x10U\xa4\xc9\x00\xd7\xd8(H\xdd"
    str_0 = "XGdP~&r1B\rG-"
    tuple_0 = (set_0, bytes_0, str_0)
    module_0.levenshtein(tuple_0, str_0)