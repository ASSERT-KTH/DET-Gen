# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_1820 as module_0
import builtins as module_1


#@pytest.mark.xfail(strict=True)
def test_case_0():
    int_0 = -333
    list_0 = [int_0, int_0, int_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == "NO"
    var_1 = module_0.func(*list_0)
    assert var_1 == "NO"
#    module_0.func()


#@pytest.mark.xfail(strict=True)
#def test_case_1():
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_2():
    int_0 = 841
    list_0 = [int_0, int_0, int_0]
    var_0 = module_1.object()
    var_1 = module_0.func(*list_0)
    assert var_1 == "NO"
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_3():
    int_0 = 820
    list_0 = [int_0, int_0, int_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == "YES"
    var_1 = module_0.func(*list_0)
    assert var_1 == "YES"
#    module_0.func()


def test_case_4():
    str_0 = "7"
    list_0 = [str_0, str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == "YES"