# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import builtins as module_0
import src_2133 as module_1


#@pytest.mark.xfail(strict=True)
def test_case_0():
    bool_0 = True
    list_0 = [bool_0, bool_0]
    object_0 = module_0.object()
    var_0 = module_1.func(*list_0)
    assert var_0 == 0
#    module_1.func()


#@pytest.mark.xfail(strict=True)
#def test_case_1():
#    module_1.func()


#@pytest.mark.xfail(strict=True)
def test_case_2():
    int_0 = 213
    list_0 = [int_0, int_0]
    var_0 = module_1.func(*list_0)
    assert var_0 == 118
#    module_1.func()
