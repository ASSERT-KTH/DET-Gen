# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_1820 as module_0
import builtins as module_1


#@pytest.mark.xfail(strict=True)
def test_case_0():
    int_0 = 514
    list_0 = [int_0, int_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == "NO"
#    module_0.func(*int_0)


#@pytest.mark.xfail(strict=True)
def test_case_1():
    list_0 = []
#    module_0.func(*list_0)


#@pytest.mark.xfail(strict=True)
def test_case_2():
    int_0 = 60
    list_0 = [int_0, int_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == "YES"
#    module_0.func(*int_0)


#@pytest.mark.xfail(strict=True)
def test_case_3():
    int_0 = 477
    list_0 = [int_0, int_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == "YES"
#    module_1.object(**list_0)
