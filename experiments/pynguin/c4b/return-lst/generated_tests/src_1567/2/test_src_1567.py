# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_1567 as module_0


def test_case_0():
    str_0 = "B~mRiuzPs"
    list_0 = [str_0, str_0]
    var_0 = module_0.func(*list_0)


def test_case_1():
    str_0 = "K<jf`:=:+6]/W-~@31M"
    var_0 = module_0.func(*str_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    module_0.func()


def test_case_3():
    str_0 = "f"
    list_0 = [str_0, str_0]
    var_0 = module_0.func(*list_0)


def test_case_4():
    str_0 = "Lr\x0bXt<*wD{Am\r"
    tuple_0 = (str_0, str_0, str_0, str_0)
    var_0 = module_0.func(*tuple_0)


def test_case_5():
    str_0 = 'ho:EJ "XyPy'
    int_0 = 1580
    tuple_0 = (str_0, int_0, int_0, int_0)
    var_0 = module_0.func(*tuple_0)


def test_case_6():
    str_0 = "/"
    tuple_0 = (str_0, str_0, str_0, str_0)
    var_0 = module_0.func(*tuple_0)


def test_case_7():
    str_0 = '"ru\n'
    list_0 = [str_0, str_0, str_0, str_0, str_0, str_0]
    var_0 = module_0.func(*list_0)


def test_case_8():
    str_0 = '"/ru\n'
    list_0 = [str_0, str_0, str_0, str_0, str_0, str_0]
    var_0 = module_0.func(*list_0)
