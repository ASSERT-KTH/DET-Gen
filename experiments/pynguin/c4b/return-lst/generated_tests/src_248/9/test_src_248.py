# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_248 as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_1():
    str_0 = "6$hoGi1G#*6$"
    module_0.func(*str_0)


def test_case_2():
    int_0 = -1048
    str_0 = "7"
    list_0 = [int_0, str_0, str_0]
    var_0 = module_0.func(*list_0)


@pytest.mark.xfail(strict=True)
def test_case_3():
    str_0 = "7"
    list_0 = [str_0, str_0]
    var_0 = module_0.func(*list_0)
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_4():
    int_0 = 1830
    str_0 = "7"
    list_0 = [int_0, str_0, str_0]
    var_0 = module_0.func(*list_0)
    module_0.func()
