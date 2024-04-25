# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import levenshtein as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    str_0 = "_[X ;/1.>CHhqE\x0c(xtS#"
    var_0 = module_0.levenshtein(str_0, str_0)
    assert var_0 == 0
    module_0.levenshtein(var_0, var_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    none_type_0 = None
    module_0.levenshtein(none_type_0, none_type_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    bytes_0 = b"\x1a}\xcf\xe8\xbf\xfa\x04\x8bD\xe3\xdc"
    bytes_1 = b"\x1a\xcf\xe8\xbf\xfa\x04\x8bD\xe3\xdc"
    module_0.levenshtein(bytes_0, bytes_1)


@pytest.mark.xfail(strict=True)
def test_case_3():
    str_0 = ""
    var_0 = module_0.levenshtein(str_0, str_0)
    assert var_0 == 0
    none_type_0 = None
    module_0.levenshtein(none_type_0, str_0)


def test_case_4():
    str_0 = "f~X$X"
    str_1 = "YogO:MDKk"
    var_0 = module_0.levenshtein(str_0, str_1)
    assert var_0 == 9