# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_2116 as module_0
import builtins as module_1


#@pytest.mark.xfail(strict=True)
#def test_case_0():
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_1():
    bool_0 = True
    dict_0 = {bool_0: bool_0, bool_0: bool_0}
    str_0 = "\nh{"
    list_0 = [bool_0, str_0, bool_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == "NO"
#    module_1.object(**dict_0)


def test_case_2():
    bool_0 = False
    list_0 = [bool_0, bool_0, bool_0, bool_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == "YES"


#@pytest.mark.xfail(strict=True)
def test_case_3():
    int_0 = 2
    set_0 = {int_0, int_0, int_0, int_0}
    list_0 = [int_0, int_0, set_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == "NO"
    bool_0 = False
    list_1 = [bool_0, bool_0, bool_0]
    var_1 = module_0.func(*list_1)
    assert var_1 == "YES"
    object_0 = module_1.object()
#    module_0.func()
