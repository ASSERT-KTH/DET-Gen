# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_391 as module_0


#@pytest.mark.xfail(strict=True)
#def test_case_0():
#    module_0.func()


def test_case_1():
    str_0 = "7wnNa+\r7"
    set_0 = {str_0, str_0, str_0, str_0, str_0}
    var_0 = module_0.func(*set_0)
    assert var_0 == 1


def test_case_2():
    str_0 = "U:wnba+\r2"
    set_0 = {str_0, str_0}
    var_0 = module_0.func(*set_0)
    assert var_0 == 2


#@pytest.mark.xfail(strict=True)
def test_case_3():
    str_0 = "Ulwnbak\r92"
    set_0 = {str_0, str_0}
    var_0 = module_0.func(*set_0)
    assert var_0 == 3
#    module_0.func()