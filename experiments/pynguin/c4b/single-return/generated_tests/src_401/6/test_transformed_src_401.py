# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_401 as module_0


#@pytest.mark.xfail(strict=True)
#def test_case_0():
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_1():
    str_0 = "8\t@tfC&"
#    module_0.func(*str_0)


#@pytest.mark.xfail(strict=True)
def test_case_2():
    str_0 = "82@t;1&"
#    module_0.func(*str_0)


#@pytest.mark.xfail(strict=True)
def test_case_3():
    str_0 = "0\x0c1"
    var_0 = module_0.func(*str_0)
    assert var_0 == 7
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_4():
    str_0 = "582@t;1&"
    var_0 = module_0.func(*str_0)
    assert var_0 == 1
#    module_0.func()
