# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_928 as module_0
import builtins as module_1


def test_case_0():
    bool_0 = True
    list_0 = [bool_0]
    var_0 = module_0.func(*list_0)


#@pytest.mark.xfail(strict=True)
def test_case_1():
    list_0 = []
    object_0 = module_1.object(*list_0)
#    module_0.func(*object_0)


#@pytest.mark.xfail(strict=True)
def test_case_2():
    bool_0 = False
    list_0 = [bool_0]
    var_0 = module_0.func(*list_0)
#    module_0.func()