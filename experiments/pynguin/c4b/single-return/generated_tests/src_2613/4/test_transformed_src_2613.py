# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_2613 as module_0


#@pytest.mark.xfail(strict=True)
def test_case_0():
    str_0 = "2U-h#Pbc\\G0"
    list_0 = [str_0, str_0, str_0, str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == 0
#    module_0.func()


#@pytest.mark.xfail(strict=True)
#def test_case_1():
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_2():
    str_0 = 'x.1V[\t=3?75"6g'
    list_0 = [str_0, str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == 0
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_3():
    str_0 = "qMh#K?$lpc2s>\\a\\o"
    list_0 = [str_0, str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == 1
#    module_0.func()
