# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_1419 as module_0


#@pytest.mark.xfail(strict=True)
def test_case_0():
    str_0 = "x"
    list_0 = [str_0, str_0, str_0]
    var_0 = module_0.func(*list_0)
    var_1 = module_0.func(*var_0)
#    module_0.func()


def test_case_1():
    str_0 = 'v"8r0['
    list_0 = [str_0, str_0, str_0]
    var_0 = module_0.func(*list_0)


#@pytest.mark.xfail(strict=True)
#def test_case_2():
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_3():
    str_0 = "jP"
    list_0 = [str_0, str_0]
    var_0 = module_0.func(*list_0)
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_4():
    str_0 = '5v"8?0*'
    list_0 = [str_0, str_0, str_0]
    none_type_0 = None
    var_0 = module_0.func(*list_0)
    var_1 = module_0.func(*list_0)
#    module_0.func(*none_type_0)