# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_1419 as module_0
import builtins as module_1


@pytest.mark.xfail(strict=True)
def test_case_0():
    module_0.func()


def test_case_1():
    str_0 = "|"
    var_0 = module_0.func(*str_0)
    var_1 = module_0.func(*var_0)
    var_2 = module_0.func(*str_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    str_0 = "\taZQ[^dF"
    list_0 = [str_0, str_0]
    list_1 = [list_0, list_0, list_0, list_0]
    var_0 = module_0.func(*list_1)
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_3():
    str_0 = "Z(L-}h+g&0=_injOl_\x0c"
    var_0 = module_0.func(*str_0)
    var_1 = module_1.object()
    var_2 = module_0.func(*var_0)
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_4():
    str_0 = "|VVk"
    none_type_0 = None
    list_0 = [str_0, none_type_0, str_0]
    var_0 = module_0.func(*list_0)
    var_1 = module_0.func(*str_0)
    object_0 = module_1.object()
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_5():
    str_0 = "\t7ZQ\t^|F"
    list_0 = [str_0, str_0]
    list_1 = [list_0, list_0, list_0, list_0, str_0]
    var_0 = module_0.func(*list_1)
    module_0.func()
