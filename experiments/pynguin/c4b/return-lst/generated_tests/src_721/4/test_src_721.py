# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_721 as module_0
import builtins as module_1


@pytest.mark.xfail(strict=True)
def test_case_0():
    module_0.func()


def test_case_1():
    int_0 = 2089
    set_0 = {int_0, int_0}
    tuple_0 = (int_0, int_0, set_0)
    list_0 = [int_0, tuple_0, int_0, int_0, set_0, tuple_0, set_0]
    var_0 = module_0.func(*list_0)
    list_1 = [int_0, var_0, list_0, var_0]
    var_1 = module_0.func(*list_1)


@pytest.mark.xfail(strict=True)
def test_case_2():
    bool_0 = True
    str_0 = ""
    tuple_0 = (bool_0, str_0)
    var_0 = module_0.func(*tuple_0)
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_3():
    bool_0 = False
    str_0 = "4"
    tuple_0 = (bool_0, str_0)
    var_0 = module_0.func(*tuple_0)
    object_0 = module_1.object()
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_4():
    str_0 = "4"
    tuple_0 = (str_0, str_0)
    var_0 = module_0.func(*tuple_0)
    module_0.func()
