# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import builtins as module_0
import src_1396 as module_1


@pytest.mark.xfail(strict=True)
def test_case_0():
    object_0 = module_0.object()
    tuple_0 = (object_0,)
    int_0 = 1726
    tuple_1 = (tuple_0, int_0)
    list_0 = [tuple_1, tuple_1, object_0]
    module_1.func(*list_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    list_0 = []
    list_1 = [list_0, list_0]
    module_1.func(*list_1)


@pytest.mark.xfail(strict=True)
def test_case_2():
    str_0 = "+FP1q4-\t\x0c"
    bool_0 = True
    int_0 = 2018
    tuple_0 = (str_0, bool_0, int_0)
    var_0 = module_1.func(*tuple_0)
    module_1.func()


@pytest.mark.xfail(strict=True)
def test_case_3():
    module_1.func()
