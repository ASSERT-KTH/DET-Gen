# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_252 as module_0
import builtins as module_1


def test_case_0():
    str_0 = ",+iqzl{"
    var_0 = module_0.func(*str_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_2():
    str_0 = "IT"
    var_0 = module_0.func(*str_0)
    module_0.func(*var_0)


@pytest.mark.xfail(strict=True)
def test_case_3():
    str_0 = "O"
    var_0 = module_0.func(*str_0)
    list_0 = [str_0]
    var_1 = module_0.func(*list_0)
    dict_0 = {}
    object_0 = module_1.object(**dict_0)
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_4():
    str_0 = "LXtA3UkprJdfG"
    var_0 = module_0.func(*str_0)
    list_0 = [str_0, str_0, var_0, var_0]
    var_1 = module_0.func(*list_0)
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_5():
    str_0 = "awX#Y"
    var_0 = module_0.func(*str_0)
    list_0 = [str_0, str_0, var_0, var_0]
    var_1 = module_0.func(*list_0)
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_6():
    str_0 = "XVsWy,mX6cEm"
    var_0 = module_0.func(*str_0)
    list_0 = [str_0, str_0, var_0, var_0]
    var_1 = module_0.func(*list_0)
    module_1.object(*str_0)
