# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_1994 as module_0
import builtins as module_1


#@pytest.mark.xfail(strict=True)
def test_case_0():
    dict_0 = {}
    bool_0 = False
    list_0 = [dict_0, bool_0, dict_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == 0
#    module_0.func()


#@pytest.mark.xfail(strict=True)
#def test_case_1():
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_2():
    object_0 = module_1.object()
    list_0 = [object_0, object_0]
    set_0 = {object_0}
    list_1 = [list_0, object_0, set_0, list_0]
#    module_0.func(*list_1)
