# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_1169 as module_0
import builtins as module_1


#@pytest.mark.xfail(strict=True)
def test_case_0():
    bool_0 = True
    list_0 = [bool_0, bool_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == 1
#    module_0.func()


#@pytest.mark.xfail(strict=True)
#def test_case_1():
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_2():
    float_0 = 527.5458
    list_0 = [float_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == 24394303
    object_0 = module_1.object()
#    module_0.func()
