# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_335 as module_0
import builtins as module_1


def test_case_0():
    str_0 = "_t[+AYd=|rr5^we9r5 "
    var_0 = module_0.func(*str_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    module_0.func()


def test_case_2():
    str_0 = "_t[+AYd=|rr5^we9r5 "
    list_0 = [str_0, str_0, str_0, str_0]
    var_0 = module_0.func(*list_0)


@pytest.mark.xfail(strict=True)
def test_case_3():
    str_0 = "QWmgFxK^9m+}\x0c~"
    list_0 = [str_0, str_0, str_0]
    var_0 = module_0.func(*list_0)
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_4():
    str_0 = ">Ioi.>dsA^'zH^="
    list_0 = [str_0, str_0]
    var_0 = module_0.func(*list_0)
    var_1 = module_1.object()
    module_0.func()
