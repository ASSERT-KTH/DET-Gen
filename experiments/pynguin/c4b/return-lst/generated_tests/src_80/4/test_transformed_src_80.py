# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_80 as module_0


def test_case_0():
    int_0 = 1592
    list_0 = [int_0, int_0, int_0]
    var_0 = module_0.func(*list_0)


#@pytest.mark.xfail(strict=True)
def test_case_1():
    bool_0 = False
    list_0 = [bool_0, bool_0, bool_0]
    var_0 = module_0.func(*list_0)
#    module_0.func()


#@pytest.mark.xfail(strict=True)
#def test_case_2():
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_3():
    int_0 = 525
    list_0 = [int_0, int_0, int_0, int_0]
    var_0 = module_0.func(*list_0)
    var_1 = module_0.func(*list_0)
#    module_0.func()