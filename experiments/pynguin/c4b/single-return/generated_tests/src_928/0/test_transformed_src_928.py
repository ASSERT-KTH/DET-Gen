# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_928 as module_0
import builtins as module_1


def test_case_0():
    bool_0 = True
    list_0 = [bool_0]
    list_1 = [bool_0, list_0]
    var_0 = module_0.func(*list_1)
    assert var_0 == 1


#@pytest.mark.xfail(strict=True)
#def test_case_1():
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_2():
    bool_0 = False
    list_0 = [bool_0]
    list_1 = [bool_0, list_0]
    var_0 = module_0.func(*list_1)
    assert var_0 == 0
#    module_1.object(**var_0)
