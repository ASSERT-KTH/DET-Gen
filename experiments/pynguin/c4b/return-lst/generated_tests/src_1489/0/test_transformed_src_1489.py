# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_1489 as module_0


def test_case_0():
    str_0 = "D"
    var_0 = module_0.func(*str_0)
    var_1 = module_0.func(*var_0)


#@pytest.mark.xfail(strict=True)
#def test_case_1():
#    module_0.func()


def test_case_2():
    str_0 = "g'(C\x0b[k)"
    list_0 = [str_0]
    var_0 = module_0.func(*list_0)


def test_case_3():
    str_0 = "g"
    var_0 = module_0.func(*str_0)


#@pytest.mark.xfail(strict=True)
def test_case_4():
    str_0 = "h>PED"
    list_0 = [str_0, str_0]
    var_0 = module_0.func(*list_0)
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_5():
    str_0 = "'/3ct("
    list_0 = [str_0]
    var_0 = module_0.func(*list_0)
#    module_0.func()