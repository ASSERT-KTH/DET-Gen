# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_2341 as module_0


#@pytest.mark.xfail(strict=True)
#def test_case_0():
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_1():
    float_0 = -3463.92
    int_0 = 1184
    dict_0 = {float_0: float_0, float_0: float_0, int_0: float_0, float_0: int_0}
    list_0 = [float_0, dict_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == 0
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_2():
    int_0 = 1184
    dict_0 = {int_0: int_0, int_0: int_0, int_0: int_0, int_0: int_0}
    list_0 = [int_0, dict_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == 0
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_3():
    int_0 = -56
    str_0 = "ot*>>Ik)OO"
    set_0 = {int_0, str_0, int_0}
    var_0 = module_0.func(*set_0)
    assert var_0 == 2
#    module_0.func()