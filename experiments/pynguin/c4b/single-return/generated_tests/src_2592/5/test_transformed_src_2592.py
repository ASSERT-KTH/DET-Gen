# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_2592 as module_0


#@pytest.mark.xfail(strict=True)
def test_case_0():
    int_0 = -4165
    list_0 = [int_0, int_0, int_0, int_0]
    bool_0 = True
    list_1 = [list_0, bool_0, bool_0]
#    module_0.func(*list_1)


#@pytest.mark.xfail(strict=True)
#def test_case_1():
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_2():
    str_0 = "999"
    bool_0 = False
    tuple_0 = (str_0, bool_0)
    var_0 = module_0.func(*tuple_0)
    assert var_0 == 999
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_3():
    str_0 = "999="
    bool_0 = True
    tuple_0 = (str_0, bool_0)
    var_0 = module_0.func(*tuple_0)
    assert var_0 == 9989
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_4():
    str_0 = "99;9"
    bool_0 = True
    tuple_0 = (str_0, bool_0)
    var_0 = module_0.func(*tuple_0)
    assert var_0 == 9899
#    module_0.func()
