# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_750 as module_0


#@pytest.mark.xfail(strict=True)
#def test_case_0():
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_1():
    str_0 = "VFZcpfc!h(="
    float_0 = -414.0
    tuple_0 = (float_0, str_0, float_0, float_0)
#    module_0.func(*tuple_0)


#@pytest.mark.xfail(strict=True)
def test_case_2():
    str_0 = "27@Q12C\x0cVw"
    var_0 = module_0.func(*str_0)
    assert var_0 == 7
#    module_0.func(*var_0)
