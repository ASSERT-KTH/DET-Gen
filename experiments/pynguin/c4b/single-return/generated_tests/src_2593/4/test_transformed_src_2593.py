# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_2593 as module_0
import builtins as module_1


def test_case_0():
    bool_0 = True
    list_0 = [bool_0, bool_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == 1


#@pytest.mark.xfail(strict=True)
def test_case_1():
    float_0 = 1448.0
    list_0 = [float_0, float_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == 999
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_2():
    float_0 = 103.4494
    list_0 = [float_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == 99
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_3():
    int_0 = 593
    list_0 = [int_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == 589
    var_1 = module_0.func(*list_0)
    assert var_1 == 589
    object_0 = module_1.object()
#    module_0.func(*object_0)


#@pytest.mark.xfail(strict=True)
def test_case_4():
    float_0 = 108.70547839045328
    list_0 = [float_0, float_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == 99
    var_1 = module_1.object()
#    module_0.func()