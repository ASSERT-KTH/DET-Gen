# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_402 as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    module_0.func()


def test_case_1():
    str_0 = "7D7-m"
    var_0 = module_0.func(*str_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    int_0 = -1449
    str_0 = ""
    list_0 = [int_0, str_0]
    var_0 = module_0.func(*list_0)
    module_0.func()


def test_case_3():
    int_0 = -1478
    str_0 = "7D-m"
    list_0 = [int_0, str_0]
    var_0 = module_0.func(*list_0)


@pytest.mark.xfail(strict=True)
def test_case_4():
    int_0 = -1444
    str_0 = "7"
    list_0 = [int_0, str_0]
    var_0 = module_0.func(*list_0)
    module_0.func()


def test_case_5():
    int_0 = -3425
    str_0 = "4o4uL'"
    list_0 = [int_0, str_0]
    var_0 = module_0.func(*list_0)