# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_529 as module_0
import builtins as module_1


def test_case_0():
    str_0 = "xkD=O`YJ_5mT"
    list_0 = [str_0, str_0, str_0, str_0]
    var_0 = module_0.func(*list_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    str_0 = "Bnq{0o7:"
    var_0 = module_0.func(*str_0)
    list_0 = [var_0, str_0, var_0]
    module_1.object(*list_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_3():
    int_0 = -208
    list_0 = [int_0, int_0, int_0, int_0, int_0, int_0]
    list_1 = [list_0, list_0]
    var_0 = module_0.func(*list_1)
    module_1.object(**list_1)


@pytest.mark.xfail(strict=True)
def test_case_4():
    int_0 = -210
    list_0 = [int_0, int_0, int_0, int_0, int_0, int_0, int_0]
    list_1 = [list_0, list_0]
    var_0 = module_0.func(*list_1)
    module_0.func()
