# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_1906 as module_0
import builtins as module_1


#@pytest.mark.xfail(strict=True)
#def test_case_0():
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_1():
    bool_0 = False
    int_0 = -1410
    list_0 = [bool_0, int_0, bool_0]
    list_1 = [list_0, bool_0, list_0, int_0]
    var_0 = module_0.func(*list_1)
    assert var_0 == "NO"
    set_0 = set()
#    module_0.func(*set_0)


#@pytest.mark.xfail(strict=True)
def test_case_2():
    str_0 = "mHKJPI\t:Q}%"
    list_0 = [str_0, str_0, str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == "YES"
#    module_1.object(*list_0)