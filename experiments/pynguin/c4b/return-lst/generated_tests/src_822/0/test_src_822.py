# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_822 as module_0
import builtins as module_1


@pytest.mark.xfail(strict=True)
def test_case_0():
    module_0.func()


def test_case_1():
    bool_0 = False
    list_0 = [bool_0, bool_0]
    var_0 = module_0.func(*list_0)


def test_case_2():
    bool_0 = True
    list_0 = [bool_0]
    var_0 = module_0.func(*list_0)
    var_1 = module_1.object()


def test_case_3():
    bool_0 = True
    list_0 = [bool_0, bool_0, bool_0, bool_0]
    var_0 = module_0.func(*list_0)
    var_1 = module_0.func(*var_0)


@pytest.mark.xfail(strict=True)
def test_case_4():
    bool_0 = True
    list_0 = [bool_0, bool_0, bool_0, bool_0]
    var_0 = module_0.func(*list_0)
    var_1 = module_0.func(*var_0)
    var_2 = module_0.func(*var_1)
    var_3 = module_0.func(*var_0)
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_5():
    int_0 = -2653
    list_0 = [int_0, int_0]
    var_0 = module_0.func(*list_0)
    list_1 = [var_0, var_0, var_0]
    module_0.func(*list_1)