# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_81 as module_0
import builtins as module_1


def test_case_0():
    str_0 = "29\x0b2"
    list_0 = [str_0, str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == 1


#@pytest.mark.xfail(strict=True)
#def test_case_1():
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_2():
    str_0 = "29\x0b20"
    list_0 = [str_0, str_0, str_0, str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == 5
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_3():
    str_0 = "29\x0b0"
    list_0 = [str_0, str_0, str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == 0
    object_0 = module_1.object()
    object_1 = module_1.object()
#    module_0.func()
