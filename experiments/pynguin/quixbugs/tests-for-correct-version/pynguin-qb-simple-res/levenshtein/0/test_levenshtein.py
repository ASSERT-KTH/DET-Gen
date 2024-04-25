# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import levenshtein as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    str_0 = "%U#/B \r"
    var_0 = module_0.levenshtein(str_0, str_0)
    assert var_0 == 0
    module_0.levenshtein(var_0, var_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    none_type_0 = None
    module_0.levenshtein(none_type_0, none_type_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    bytes_0 = b"\x89T\x93lG"
    module_0.levenshtein(bytes_0, bytes_0)


@pytest.mark.xfail(strict=True)
def test_case_3():
    complex_0 = 2.84468 + 2463j
    str_0 = "r(!}`?!"
    tuple_0 = (complex_0, str_0)
    dict_0 = {}
    bool_0 = False
    tuple_1 = (tuple_0, dict_0, bool_0, tuple_0)
    module_0.levenshtein(tuple_1, tuple_0)


@pytest.mark.xfail(strict=True)
def test_case_4():
    str_0 = "gp\x0b\r$u`IPM\t)`DF"
    str_1 = ""
    var_0 = module_0.levenshtein(str_0, str_1)
    assert var_0 == 15
    int_0 = 30
    none_type_0 = None
    module_0.levenshtein(int_0, none_type_0)