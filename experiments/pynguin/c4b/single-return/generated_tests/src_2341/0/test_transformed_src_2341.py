# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_2341 as module_0
import builtins as module_1


#@pytest.mark.xfail(strict=True)
def test_case_0():
    int_0 = 3079
    list_0 = [int_0, int_0]
    list_1 = [int_0, list_0]
    var_0 = module_0.func(*list_1)
    assert var_0 == 1
#    module_0.func(*list_0)


#@pytest.mark.xfail(strict=True)
#def test_case_1():
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_2():
    int_0 = 3095
    list_0 = [int_0, int_0, int_0, int_0]
    list_1 = [int_0, list_0]
    var_0 = module_0.func(*list_1)
    assert var_0 == 3
    int_1 = 2363
    list_2 = [list_1, int_1, int_1, list_1]
#    module_0.func(*list_2)


#@pytest.mark.xfail(strict=True)
def test_case_3():
    int_0 = 3095
    list_0 = [int_0]
    list_1 = [int_0, list_0]
    var_0 = module_0.func(*list_1)
    assert var_0 == 0
    object_0 = module_1.object()
#    module_1.object(*list_1, **var_0)


#@pytest.mark.xfail(strict=True)
def test_case_4():
    int_0 = 3097
    list_0 = [int_0, int_0]
    list_1 = [int_0, list_0]
    var_0 = module_0.func(*list_1)
    assert var_0 == 1
    int_1 = 2363
    list_2 = [var_0, list_1, int_1, int_1, var_0, list_1]
    var_1 = module_0.func(*list_2)
    assert var_1 == 0
#    module_0.func()
