# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_401 as module_0
import builtins as module_1


@pytest.mark.xfail(strict=True)
def test_case_0():
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_1():
    str_0 = "0"
    list_0 = [str_0, str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == 7
    var_1 = module_1.object()
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_2():
    str_0 = "0"
    list_0 = [str_0, str_0, str_0, str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == 7
    list_1 = [var_0, str_0]
    module_0.func(*list_1)


@pytest.mark.xfail(strict=True)
def test_case_3():
    str_0 = "9"
    list_0 = [str_0, str_0, str_0, str_0, str_0, str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == 1
    module_0.func(*var_0)
