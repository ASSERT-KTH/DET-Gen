# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_1623 as module_0


#@pytest.mark.xfail(strict=True)
def test_case_0():
    int_0 = 3174
    list_0 = [int_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == 1587
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_1():
    bool_0 = True
    list_0 = [bool_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == 1
    list_1 = [bool_0, var_0, bool_0, list_0]
    list_2 = [list_1, list_1]
#    module_0.func(*list_2)


#@pytest.mark.xfail(strict=True)
#def test_case_2():
#    module_0.func()
