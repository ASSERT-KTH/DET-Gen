# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_2426 as module_0
import builtins as module_1


@pytest.mark.xfail(strict=True)
def test_case_0():
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_1():
    str_0 = "1i]{,i8bt"
    module_0.func(*str_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    str_0 = '0.xK2(",\t'
    var_0 = module_0.func(*str_0)
    var_1 = module_0.func(*str_0)
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_3():
    str_0 = "9\n0"
    list_0 = [str_0, str_0]
    module_0.func(*list_0)


def test_case_4():
    str_0 = "940"
    list_0 = [str_0, str_0]
    var_0 = module_0.func(*list_0)
    var_1 = module_0.func(*list_0)


@pytest.mark.xfail(strict=True)
def test_case_5():
    str_0 = "3\n05"
    list_0 = [str_0, str_0, str_0, str_0, str_0]
    var_0 = module_0.func(*list_0)
    module_1.object(**var_0)


def test_case_6():
    str_0 = "3\n0\x0b5"
    list_0 = [str_0, str_0, str_0]
    var_0 = module_0.func(*list_0)


def test_case_7():
    str_0 = "8\n0\x0b5"
    list_0 = [str_0]
    var_0 = module_0.func(*list_0)


@pytest.mark.xfail(strict=True)
def test_case_8():
    str_0 = "8\n5\x0b5"
    list_0 = [str_0]
    var_0 = module_0.func(*list_0)
    object_0 = module_1.object()
    var_1 = module_0.func(*list_0)
    module_0.func()