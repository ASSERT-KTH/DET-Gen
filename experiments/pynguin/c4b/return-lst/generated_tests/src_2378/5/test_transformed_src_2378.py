# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import builtins as module_0
import src_2378 as module_1


#@pytest.mark.xfail(strict=True)
def test_case_0():
    int_0 = 1193
    object_0 = module_0.object()
    tuple_0 = (object_0,)
    list_0 = [int_0, tuple_0, int_0]
    var_0 = module_1.func(*list_0)
#    module_1.func()


#@pytest.mark.xfail(strict=True)
def test_case_1():
    bool_0 = False
    list_0 = [bool_0]
    var_0 = module_1.func(*list_0)
    var_1 = module_1.func(*list_0)
#    module_1.func()


#@pytest.mark.xfail(strict=True)
#def test_case_2():
#    module_1.func()
