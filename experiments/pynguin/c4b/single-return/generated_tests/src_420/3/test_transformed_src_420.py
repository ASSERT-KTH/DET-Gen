# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_420 as module_0


#@pytest.mark.xfail(strict=True)
def test_case_0():
    bool_0 = True
    list_0 = [bool_0, bool_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == 1
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_1():
    float_0 = -455.3434
    int_0 = -26
    list_0 = [float_0, int_0, int_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == 0
    list_1 = []
#    module_0.func(*list_1)


#@pytest.mark.xfail(strict=True)
#def test_case_2():
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_3():
    int_0 = 567
    list_0 = [int_0, int_0, int_0, int_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == 30381183
#    module_0.func()
