# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_1946 as module_0
import builtins as module_1


@pytest.mark.xfail(strict=True)
def test_case_0():
    module_0.func()


def test_case_1():
    str_0 = "5e"
    list_0 = [str_0, str_0, str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == 18


@pytest.mark.xfail(strict=True)
def test_case_2():
    str_0 = "54{"
    list_0 = [str_0, str_0, str_0, str_0, str_0, str_0]
    module_0.func(*list_0)


@pytest.mark.xfail(strict=True)
def test_case_3():
    str_0 = "4{"
    list_0 = [str_0, str_0, str_0, str_0, str_0, str_0]
    module_0.func(*list_0)


@pytest.mark.xfail(strict=True)
def test_case_4():
    str_0 = "15e"
    list_0 = [str_0, str_0, str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == 50
    object_0 = module_1.object()
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_5():
    str_0 = "4e"
    list_0 = [str_0, str_0, str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == 9
    module_0.func()
