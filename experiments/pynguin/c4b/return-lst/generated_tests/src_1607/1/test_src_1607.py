# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_1607 as module_0
import builtins as module_1


@pytest.mark.xfail(strict=True)
def test_case_0():
    module_0.func()


def test_case_1():
    bool_0 = False
    list_0 = [bool_0]
    var_0 = module_0.func(*list_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    str_0 = "3\rGd8em4Z]6("
    var_0 = module_0.func(*str_0)
    var_1 = module_0.func(*str_0)
    var_2 = module_0.func(*str_0)
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_3():
    bool_0 = True
    list_0 = [bool_0, bool_0, bool_0]
    var_0 = module_0.func(*list_0)
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_4():
    int_0 = -122
    list_0 = [int_0, int_0, int_0]
    var_0 = module_0.func(*list_0)
    module_1.object(**int_0)


@pytest.mark.xfail(strict=True)
def test_case_5():
    str_0 = "2X\rG`8e\x0b4Z]0("
    var_0 = module_0.func(*str_0)
    var_1 = module_0.func(*var_0)
    module_0.func()