# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_2339 as module_0


def test_case_0():
    str_0 = 'uc=TM!N\x0b"x:ufZ$J'
    var_0 = module_0.func(*str_0)
    assert var_0 == "NO"


@pytest.mark.xfail(strict=True)
def test_case_1():
    dict_0 = {}
    list_0 = [dict_0]
    module_0.func(*list_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    module_0.func()


def test_case_3():
    str_0 = 'uc =TM!N\x0b"x:ufZ$J'
    list_0 = [str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == "NO"


def test_case_4():
    str_0 = "\rQw]lwZ\t"
    list_0 = [str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == "YES"
    list_1 = [var_0]
    var_1 = module_0.func(*list_1)
    assert var_1 == "NO"
