# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_1906 as module_0


def test_case_0():
    dict_0 = {}
    str_0 = "[r;K(lI@!y\ta2KmFA2"
    list_0 = [str_0, dict_0, dict_0, str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == "NO"
    list_1 = [dict_0, dict_0, dict_0, dict_0]
    var_1 = module_0.func(*list_1)
    assert var_1 == "NO"


def test_case_1():
    dict_0 = {}
    list_0 = [dict_0, dict_0, dict_0, dict_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == "NO"


@pytest.mark.xfail(strict=True)
def test_case_2():
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_3():
    str_0 = "c/jYmaih48o\ty)Hw5$"
    list_0 = [str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == "YES"
    module_0.func()
