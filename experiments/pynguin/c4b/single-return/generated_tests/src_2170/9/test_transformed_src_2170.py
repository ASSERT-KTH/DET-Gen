# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_2170 as module_0


def test_case_0():
    float_0 = 239.2
    complex_0 = 784 + 1272.9827j
    list_0 = [float_0, float_0, complex_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == 515523


#@pytest.mark.xfail(strict=True)
#def test_case_1():
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_2():
    bool_0 = False
    list_0 = [bool_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == 1
#    module_0.func()
