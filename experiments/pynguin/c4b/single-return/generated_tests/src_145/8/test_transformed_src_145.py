# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_145 as module_0
import builtins as module_1


def test_case_0():
    int_0 = -5
    list_0 = [int_0, int_0, int_0, int_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == 3


#@pytest.mark.xfail(strict=True)
def test_case_1():
    int_0 = 435
    list_0 = [int_0, int_0, int_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == 2
#    module_1.object(**var_0)


#@pytest.mark.xfail(strict=True)
#def test_case_2():
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_3():
    int_0 = 8
    list_0 = [int_0, int_0, int_0, int_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == 2
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_4():
    int_0 = 19
    list_0 = [int_0, int_0, int_0, int_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == 1
    var_1 = module_1.object()
#    module_0.func(*int_0)


#@pytest.mark.xfail(strict=True)
def test_case_5():
    int_0 = 169
    list_0 = [int_0, int_0, int_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == 2
    var_1 = module_0.func(*list_0)
    assert var_1 == 2
    list_1 = [var_0, int_0, list_0]
    var_2 = module_0.func(*list_1)
    assert var_2 == 1
#    module_0.func()
