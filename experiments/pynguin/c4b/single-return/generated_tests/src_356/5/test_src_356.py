# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_356 as module_0


def test_case_0():
    str_0 = "m9F4\\sXtC;UZ7"
    var_0 = module_0.func(*str_0)
    assert var_0 == "M"


@pytest.mark.xfail(strict=True)
def test_case_1():
    str_0 = "R1"
    var_0 = module_0.func(*str_0)
    assert var_0 == "r"
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_2():
    module_0.func()


def test_case_3():
    str_0 = "<l#Exf\x0bLl$S_S)\\ET"
    var_0 = module_0.func(*str_0)
    assert var_0 == "<"


@pytest.mark.xfail(strict=True)
def test_case_4():
    str_0 = "R1"
    list_0 = [str_0, str_0, str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == "r1"
    var_1 = module_0.func(*var_0)
    assert var_1 == "R"
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_5():
    str_0 = "oE"
    list_0 = [str_0, str_0, str_0, str_0, str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == "Oe"
    var_1 = module_0.func(*var_0)
    assert var_1 == "o"
    module_0.func()
