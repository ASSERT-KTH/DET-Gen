# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import shunting_yard as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    str_0 = "[gI|"
    module_0.shunting_yard(str_0)


def test_case_1():
    list_0 = []
    var_0 = module_0.shunting_yard(list_0)


def test_case_2():
    str_0 = "V"
    var_0 = module_0.shunting_yard(str_0)


def test_case_3():
    int_0 = 1392
    tuple_0 = (int_0, int_0)
    var_0 = module_0.shunting_yard(tuple_0)


@pytest.mark.xfail(strict=True)
def test_case_4():
    str_0 = "**`)&)5"
    module_0.shunting_yard(str_0)


@pytest.mark.xfail(strict=True)
def test_case_5():
    str_0 = "+**`)&5"
    module_0.shunting_yard(str_0)


@pytest.mark.xfail(strict=True)
def test_case_6():
    str_0 = ".9YHu&DP\tC Wis]"
    bytes_0 = b"\xe1~~\xbe\xb4\xf2vPw\xa3"
    var_0 = module_0.shunting_yard(bytes_0)
    list_0 = [str_0]
    var_1 = module_0.shunting_yard(list_0)
    str_1 = "+**-`)&5"
    module_0.shunting_yard(str_1)