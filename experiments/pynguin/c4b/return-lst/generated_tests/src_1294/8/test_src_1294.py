# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_1294 as module_0
import builtins as module_1


def test_case_0():
    str_0 = "y"
    var_0 = module_0.func(*str_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_2():
    str_0 = "ky"
    module_0.func(*str_0)


@pytest.mark.xfail(strict=True)
def test_case_3():
    str_0 = "u1Gy#"
    var_0 = module_0.func(*str_0)
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_4():
    str_0 = "i"
    var_0 = module_0.func(*str_0)
    tuple_0 = ()
    list_0 = [str_0, str_0, str_0, tuple_0]
    var_1 = module_0.func(*list_0)
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_5():
    str_0 = "e"
    var_0 = module_0.func(*str_0)
    module_0.func(*var_0)


def test_case_6():
    str_0 = "oy"
    var_0 = module_0.func(*str_0)
    var_1 = module_1.object()


@pytest.mark.xfail(strict=True)
def test_case_7():
    str_0 = "aA"
    var_0 = module_0.func(*str_0)
    module_0.func()
