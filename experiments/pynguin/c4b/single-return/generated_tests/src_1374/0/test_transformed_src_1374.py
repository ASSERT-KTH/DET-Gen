# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_1374 as module_0


#@pytest.mark.xfail(strict=True)
def test_case_0():
    int_0 = -2686
    list_0 = [int_0, int_0, int_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == -672
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_1():
    int_0 = 1505
    list_0 = [int_0, int_0, int_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == 0
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_2():
    none_type_0 = None
#    module_0.func(*none_type_0)


#@pytest.mark.xfail(strict=True)
def test_case_3():
    int_0 = 450
    list_0 = [int_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == 112
    none_type_0 = None
    var_1 = module_0.func(*list_0)
    assert var_1 == 112
    var_2 = module_0.func(*list_0)
    assert var_2 == 112
    list_1 = [var_1, none_type_0, list_0, none_type_0]
    var_3 = module_0.func(*list_1)
    assert var_3 == 27
#    module_0.func()