# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_2157 as module_0
import builtins as module_1


def test_case_0():
    float_0 = 416.867
    list_0 = [float_0, float_0]
    var_0 = module_0.func(*list_0)
    var_1 = module_0.func(*var_0)


#@pytest.mark.xfail(strict=True)
#def test_case_1():
#    module_0.func()


def test_case_2():
    float_0 = 416.867
    list_0 = [float_0, float_0]
    var_0 = module_0.func(*list_0)


#@pytest.mark.xfail(strict=True)
def test_case_3():
    float_0 = 21.744695859393644
    list_0 = [float_0]
    var_0 = module_0.func(*list_0)
    object_0 = module_1.object()
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_4():
    float_0 = 15.995851300016087
    list_0 = [float_0, float_0]
    var_0 = module_0.func(*list_0)
#    module_1.object(*list_0)


#@pytest.mark.xfail(strict=True)
def test_case_5():
    float_0 = 20.387783140404473
    list_0 = [float_0]
    var_0 = module_0.func(*list_0)
    object_0 = module_1.object()
#    module_0.func()