# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_1325 as module_0
import builtins as module_1


@pytest.mark.xfail(strict=True)
def test_case_0():
    module_0.func()


def test_case_1():
    str_0 = "9A^5zI&P n RD"
    var_0 = module_0.func(*str_0)


def test_case_2():
    str_0 = "91^[zI&P n RD"
    object_0 = module_0.func(*str_0)


@pytest.mark.xfail(strict=True)
def test_case_3():
    str_0 = "13WQU958e1\n5"
    var_0 = module_0.func(*str_0)
    module_0.func()


def test_case_4():
    str_0 = "01^yzI&D nZg"
    int_0 = 2
    set_0 = {str_0, int_0, str_0}
    var_0 = module_0.func(*set_0)


@pytest.mark.xfail(strict=True)
def test_case_5():
    str_0 = "91^yzI&\\ n gJ"
    int_0 = -457
    list_0 = [int_0, str_0]
    var_0 = module_0.func(*list_0)
    module_1.object(*list_0)
