# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_2375 as module_0
import builtins as module_1


def test_case_0():
    str_0 = "%o1~p"
    list_0 = [str_0, str_0, str_0, str_0]
    var_0 = module_0.func(*list_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    bool_0 = False
    module_0.func(*bool_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    str_0 = "T:E&\n3lOH"
    list_0 = [str_0]
    var_0 = module_0.func(*list_0)
    var_1 = module_0.func(*str_0)
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_3():
    str_0 = "32x+~wMPqRM0U{QfO"
    list_0 = [str_0]
    var_0 = module_0.func(*list_0)
    var_1 = module_0.func(*str_0)
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_4():
    str_0 = "9:E&\n3lOH"
    var_0 = module_0.func(*str_0)
    module_1.object(**var_0)
