# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_229 as module_0


#@pytest.mark.xfail(strict=True)
def test_case_0():
    float_0 = -1811.247721221121
    list_0 = [float_0, float_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == 15
#    module_0.func()


#@pytest.mark.xfail(strict=True)
#def test_case_1():
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_2():
    int_0 = 297
    list_0 = [int_0, int_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == 7
#    module_0.func(*var_0)
