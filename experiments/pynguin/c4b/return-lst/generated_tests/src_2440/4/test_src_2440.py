# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_2440 as module_0


def test_case_0():
    str_0 = "fRW)%AN>"
    str_1 = "*B"
    list_0 = [str_1, str_0, str_1, str_1]
    var_0 = module_0.func(*list_0)


def test_case_1():
    str_0 = "fRU)%5qk"
    var_0 = module_0.func(*str_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_3():
    str_0 = "fRU)%5qk"
    set_0 = {str_0}
    var_0 = module_0.func(*set_0)
    module_0.func()


def test_case_4():
    str_0 = "R)%5k"
    var_0 = module_0.func(*str_0)


@pytest.mark.xfail(strict=True)
def test_case_5():
    str_0 = "YX&0"
    str_1 = "G+-s?#Vl^"
    list_0 = [str_0, str_0, str_1]
    var_0 = module_0.func(*list_0)
    var_1 = module_0.func(*str_0)
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_6():
    str_0 = "X"
    list_0 = [str_0, str_0, str_0, str_0]
    str_1 = "&xbhwb1]J1EKU7"
    tuple_0 = (list_0, str_0, str_1, str_0)
    var_0 = module_0.func(*tuple_0)
    module_0.func()
