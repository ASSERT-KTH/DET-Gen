# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_510 as module_0


#@pytest.mark.xfail(strict=True)
def test_case_0():
    bool_0 = False
    list_0 = [bool_0]
    var_0 = module_0.func(*list_0)
    var_1 = module_0.func(*list_0)
    var_2 = module_0.func(*list_0)
#    module_0.func()


def test_case_1():
    int_0 = 845
    set_0 = {int_0}
    tuple_0 = (set_0,)
    list_0 = [int_0, int_0, tuple_0]
    var_0 = module_0.func(*list_0)


#@pytest.mark.xfail(strict=True)
#def test_case_2():
#    module_0.func()


def test_case_3():
    int_0 = 818
    set_0 = {int_0}
    tuple_0 = (set_0,)
    list_0 = [int_0, int_0, tuple_0]
    var_0 = module_0.func(*list_0)


#@pytest.mark.xfail(strict=True)
def test_case_4():
    int_0 = -732
    list_0 = [int_0, int_0]
    var_0 = module_0.func(*list_0)
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_5():
    int_0 = -732
    list_0 = [int_0, int_0]
    var_0 = module_0.func(*list_0)
    var_1 = module_0.func(*var_0)
    float_0 = -469.9129
    list_1 = [float_0]
    var_2 = module_0.func(*list_1)
#    module_0.func()
