# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_2085 as module_0
import builtins as module_1


#@pytest.mark.xfail(strict=True)
#def test_case_0():
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_1():
    bool_0 = True
    tuple_0 = (bool_0, bool_0)
    list_0 = [tuple_0, tuple_0]
    list_1 = [list_0, tuple_0]
    var_0 = module_0.func(*list_1)
    assert var_0 == "NO"
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_2():
    str_0 = '\tZwV\x0c9"fZ%Qy#BR`k"'
    set_0 = {str_0, str_0, str_0}
    var_0 = module_0.func(*set_0)
    assert var_0 == "YES"
#    module_1.object(**var_0)


#@pytest.mark.xfail(strict=True)
def test_case_3():
    str_0 = "9<X"
    set_0 = {str_0, str_0, str_0}
    var_0 = module_0.func(*set_0)
    assert var_0 == "YES"
    str_1 = "v2rvLq]H"
    list_0 = [str_1, str_1]
    var_1 = module_0.func(*list_0)
    assert var_1 == "YES"
#    module_1.object(*var_0)
