# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_2104 as module_0
import builtins as module_1


@pytest.mark.xfail(strict=True)
def test_case_0():
    module_0.func()


def test_case_1():
    str_0 = "JR\x0c)B{p\x0b5FXt1"
    list_0 = [str_0, str_0, str_0]
    var_0 = module_0.func(*list_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    str_0 = "JR\x0c2H)B{p\x0b5FXt1"
    list_0 = [str_0, str_0, str_0]
    var_0 = module_0.func(*list_0)
    module_1.object(**list_0)


@pytest.mark.xfail(strict=True)
def test_case_3():
    str_0 = 'QZZre{By("2\rx`i\rLW"'
    var_0 = module_0.func(*str_0)
    module_0.func()


def test_case_4():
    str_0 = "Yd'|aN9*C(T\x0c.wP"
    list_0 = [str_0, str_0, str_0]
    var_0 = module_0.func(*list_0)
    var_1 = module_0.func(*var_0)
