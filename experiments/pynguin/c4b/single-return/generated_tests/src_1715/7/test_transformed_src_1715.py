# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_1715 as module_0


#@pytest.mark.xfail(strict=True)
def test_case_0():
    float_0 = -1323.6
    list_0 = [float_0, float_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == -881
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_1():
    none_type_0 = None
    list_0 = [none_type_0, none_type_0]
#    module_0.func(*list_0)


#@pytest.mark.xfail(strict=True)
def test_case_2():
    float_0 = 375.13
    list_0 = [float_0, float_0, float_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == 250
#    module_0.func()
