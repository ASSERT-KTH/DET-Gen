# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_253 as module_0
import builtins as module_1


def test_case_0():
    float_0 = -631.0
    list_0 = [float_0, float_0, float_0]
    var_0 = module_0.func(*list_0)


#@pytest.mark.xfail(strict=True)
#def test_case_1():
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_2():
    float_0 = -2038.0
    list_0 = [float_0, float_0, float_0]
    var_0 = module_0.func(*list_0)
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_3():
    bool_0 = False
    set_0 = {bool_0}
    var_0 = module_0.func(*set_0)
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_4():
    float_0 = 2392.269
    list_0 = [float_0, float_0, float_0]
    var_0 = module_0.func(*list_0)
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_5():
    float_0 = 387.8323467965078
    list_0 = [float_0, float_0, float_0]
    var_0 = module_0.func(*list_0)
    var_1 = module_0.func(*list_0)
    object_0 = module_1.object()
#    module_0.func()
