# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_540 as module_0


#@pytest.mark.xfail(strict=True)
def test_case_0():
    str_0 = "$311Q7-\rAPRV\\2s&."
    list_0 = [str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == 9
#    module_0.func()


#@pytest.mark.xfail(strict=True)
#def test_case_1():
#    module_0.func()
