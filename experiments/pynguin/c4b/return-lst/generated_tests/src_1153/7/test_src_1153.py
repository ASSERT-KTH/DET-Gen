# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_1153 as module_0
import builtins as module_1


@pytest.mark.xfail(strict=True)
def test_case_0():
    module_0.func()


def test_case_1():
    str_0 = "801 4"
    list_0 = [str_0, str_0, str_0, str_0, str_0]
    var_0 = module_0.func(*list_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    str_0 = "6 7"
    list_0 = [str_0]
    module_0.func(*list_0)


def test_case_3():
    str_0 = "01 2"
    list_0 = [str_0, str_0, str_0, str_0, str_0, str_0]
    var_0 = module_0.func(*list_0)


def test_case_4():
    str_0 = "807 -2"
    list_0 = [str_0, str_0, str_0, str_0]
    var_0 = module_0.func(*list_0)


@pytest.mark.xfail(strict=True)
def test_case_5():
    str_0 = "-03 0"
    list_0 = [str_0, str_0, str_0, str_0, str_0]
    var_0 = module_0.func(*list_0)
    object_0 = module_1.object()
    module_0.func()
