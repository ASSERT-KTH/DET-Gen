# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_2593 as module_0


#@pytest.mark.xfail(strict=True)
#def test_case_0():
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_1():
    float_0 = -601.1756852378113
    bytes_0 = b""
    list_0 = [float_0, float_0, float_0, bytes_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == -601
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_2():
    int_0 = 5364
    list_0 = [int_0, int_0, int_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == 4999
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_3():
    int_0 = 793
    list_0 = [int_0, int_0, int_0, int_0, int_0, int_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == 789
    list_1 = [var_0, list_0, var_0]
    var_1 = module_0.func(*list_1)
    assert var_1 == 789
#    module_0.func(*var_0)


#@pytest.mark.xfail(strict=True)
def test_case_4():
    int_0 = 108
    list_0 = [int_0, int_0, int_0, int_0, int_0, int_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == 99
#    module_0.func()
