# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_91 as module_0


def test_case_0():
    str_0 = "\t^r["
    list_0 = [str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == 8


@pytest.mark.xfail(strict=True)
def test_case_1():
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_2():
    str_0 = "U8T^b1nd<%@&8As[AKXa"
    tuple_0 = (str_0,)
    var_0 = module_0.func(*tuple_0)
    assert var_0 == 5
    module_0.func()


def test_case_3():
    str_0 = "hZ`4&=cZEq3]c_cm@x"
    tuple_0 = (str_0,)
    var_0 = module_0.func(*tuple_0)
    assert var_0 == 5


def test_case_4():
    str_0 = "aqol0U(;T(_)\\\x0bBEUto="
    tuple_0 = (str_0,)
    var_0 = module_0.func(*tuple_0)
    assert var_0 == 5


def test_case_5():
    str_0 = "\r1zT_"
    tuple_0 = (str_0,)
    var_0 = module_0.func(*tuple_0)
    assert var_0 == 5


@pytest.mark.xfail(strict=True)
def test_case_6():
    str_0 = "h1`M#=c[hEq3}cCm@x"
    tuple_0 = (str_0,)
    var_0 = module_0.func(*tuple_0)
    assert var_0 == 3
    module_0.func()
