# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_2394 as module_0
import builtins as module_1


def test_case_0():
    str_0 = ";[aK\nQQQ\x0cN]"
    list_0 = [str_0, str_0, str_0, str_0]
    var_0 = module_0.func(*list_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_2():
    str_0 = ";[aK\nQQ}Q\x0cN]"
    list_0 = [str_0, str_0, str_0, str_0, str_0, str_0, str_0]
    var_0 = module_0.func(*list_0)
    list_1 = [list_0]
    var_1 = module_0.func(*list_1)
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_3():
    str_0 = "\r[aK\nQQQQQQQX"
    list_0 = [str_0, str_0, str_0, str_0, str_0, str_0, str_0]
    list_1 = [list_0, list_0]
    var_0 = module_0.func(*list_1)
    var_1 = module_0.func(*list_0)
    object_0 = module_1.object()
    var_2 = module_0.func(*list_1)
    module_0.func()
