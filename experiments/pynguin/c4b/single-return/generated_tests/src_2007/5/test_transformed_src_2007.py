# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_2007 as module_0


#@pytest.mark.xfail(strict=True)
def test_case_0():
    int_0 = 256
    list_0 = [int_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == "4777777777777777777777777777777777777"
    list_1 = [list_0, list_0, int_0, list_0]
#    module_0.func(*list_1)


#@pytest.mark.xfail(strict=True)
def test_case_1():
    float_0 = -3459.68
    dict_0 = {float_0: float_0}
    var_0 = module_0.func(*dict_0)
    assert var_0 == -1
#    module_0.func()


#@pytest.mark.xfail(strict=True)
#def test_case_2():
#    module_0.func()
