# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_1307 as module_0
import builtins as module_1


def test_case_0():
    str_0 = "I.OHn} Ns$^["
    tuple_0 = (str_0, str_0, str_0, str_0)
    var_0 = module_0.func(*tuple_0)


#@pytest.mark.xfail(strict=True)
#def test_case_1():
#    module_0.func()


def test_case_2():
    object_0 = module_1.object()
    str_0 = "I.OHn} Ns$^["
    tuple_0 = (object_0, str_0, str_0, object_0)
    var_0 = module_0.func(*tuple_0)


def test_case_3():
    float_0 = -2425.0
    tuple_0 = (float_0, float_0, float_0, float_0)
    list_0 = [tuple_0, tuple_0, float_0]
    var_0 = module_0.func(*list_0)


#@pytest.mark.xfail(strict=True)
def test_case_4():
    int_0 = 2042
    set_0 = {int_0, int_0, int_0, int_0}
    list_0 = [set_0, int_0, set_0, set_0]
    var_0 = module_0.func(*list_0)
    object_0 = module_1.object()
    int_1 = 2243
    tuple_0 = (object_0, object_0, object_0, int_1)
    list_1 = [tuple_0, var_0, tuple_0]
    var_1 = module_0.func(*list_1)
#    module_0.func()