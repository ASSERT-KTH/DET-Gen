# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_177 as module_0
import builtins as module_1


#@pytest.mark.xfail(strict=True)
def test_case_0():
    str_0 = "Om\x0c/{6-KFd@V#"
    var_0 = module_0.func(*str_0)
    assert var_0 == 1
#    module_0.func()


#@pytest.mark.xfail(strict=True)
#def test_case_1():
#    module_0.func()


def test_case_2():
    object_0 = module_1.object()
    list_0 = [object_0, object_0, object_0]
    int_0 = -663
    list_1 = [list_0, object_0, int_0, object_0]
    var_0 = module_0.func(*list_1)
    assert var_0 == 4
