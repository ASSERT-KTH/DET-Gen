# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_2592 as module_0


#@pytest.mark.xfail(strict=True)
def test_case_0():
    str_0 = "6m"
    list_0 = [str_0, str_0, str_0, str_0, str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == 59
    object_0 = module_0.func(*str_0)
    assert object_0 == 6
#    module_0.func()


#@pytest.mark.xfail(strict=True)
#def test_case_1():
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_2():
    str_0 = "AskmaF])#"
    list_0 = [str_0, str_0, str_0]
#    module_0.func(*list_0)


#@pytest.mark.xfail(strict=True)
def test_case_3():
    str_0 = "999999999"
    list_0 = [str_0, str_0, str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == 999999999
#    module_0.func(*var_0)


#@pytest.mark.xfail(strict=True)
def test_case_4():
    str_0 = "]8"
    list_0 = [str_0, str_0, str_0, str_0]
#    module_0.func(*list_0)


#@pytest.mark.xfail(strict=True)
def test_case_5():
    str_0 = "9999999%9"
    list_0 = [str_0, str_0, str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == 999999899
#    module_0.func(*var_0)
