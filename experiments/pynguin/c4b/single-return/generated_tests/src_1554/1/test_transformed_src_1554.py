# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_1554 as module_0
import builtins as module_1


def test_case_0():
    str_0 = '7;G1Yi=&"F3C)i'
    var_0 = module_0.func(*str_0)
    assert var_0 == 1


#@pytest.mark.xfail(strict=True)
def test_case_1():
    float_0 = -1192.219033
    list_0 = [float_0, float_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == 0
#    module_0.func()


#@pytest.mark.xfail(strict=True)
#def test_case_2():
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_3():
    bool_0 = True
    list_0 = [bool_0, bool_0, bool_0, bool_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == 1
    float_0 = 1363.6
    list_1 = [float_0, float_0]
    var_1 = module_0.func(*list_1)
    assert var_1 == 15
    var_2 = module_1.object()
#    module_0.func()
