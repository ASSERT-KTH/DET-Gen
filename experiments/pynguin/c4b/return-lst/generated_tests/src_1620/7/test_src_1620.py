# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_1620 as module_0
import builtins as module_1


@pytest.mark.xfail(strict=True)
def test_case_0():
    str_0 = "os"
    list_0 = [str_0]
    var_0 = module_0.func(*list_0)
    int_0 = -1275
    module_0.func(*int_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    bool_0 = False
    list_0 = [bool_0, bool_0]
    list_1 = [list_0, bool_0, list_0]
    module_0.func(*list_1)


@pytest.mark.xfail(strict=True)
def test_case_2():
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_3():
    str_0 = "g\\"
    list_0 = [str_0, str_0, str_0, str_0]
    var_0 = module_0.func(*list_0)
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_4():
    str_0 = "g\\"
    var_0 = module_0.func(*str_0)
    list_0 = module_0.func(*var_0)
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_5():
    str_0 = "g\\"
    list_0 = [str_0, str_0]
    var_0 = module_0.func(*list_0)
    list_1 = [var_0, var_0]
    var_1 = module_0.func(*list_1)
    module_1.object(*list_0)