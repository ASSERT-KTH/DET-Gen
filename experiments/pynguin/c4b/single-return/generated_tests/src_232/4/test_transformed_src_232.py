# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_232 as module_0
import builtins as module_1


def test_case_0():
    bool_0 = False
    list_0 = [bool_0, bool_0, bool_0, bool_0]
    var_0 = module_0.func(*list_0)


#@pytest.mark.xfail(strict=True)
#def test_case_1():
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_2():
    int_0 = -1010
    list_0 = [int_0, int_0, int_0, int_0]
    var_0 = module_0.func(*list_0)
    bool_0 = True
    list_1 = [bool_0, bool_0]
    var_1 = module_0.func(*list_1)
#    module_1.object(**bool_0)


#@pytest.mark.xfail(strict=True)
def test_case_3():
    int_0 = 2323
    list_0 = [int_0]
    var_0 = module_0.func(*list_0)
    bool_0 = True
#    module_0.func(*bool_0)
