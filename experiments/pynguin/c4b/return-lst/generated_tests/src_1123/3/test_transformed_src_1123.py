# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_1123 as module_0


def test_case_0():
    int_0 = 1756
    list_0 = [int_0]
    var_0 = module_0.func(*list_0)


#@pytest.mark.xfail(strict=True)
#def test_case_1():
#    module_0.func()


def test_case_2():
    int_0 = 1756
    list_0 = [int_0]
    var_0 = module_0.func(*list_0)
    var_1 = module_0.func(*var_0)


#@pytest.mark.xfail(strict=True)
def test_case_3():
    int_0 = 1759
    list_0 = [int_0]
    var_0 = module_0.func(*list_0)
#    module_0.func()


def test_case_4():
    int_0 = 1713
    list_0 = [int_0]
    var_0 = module_0.func(*list_0)
    var_1 = module_0.func(*var_0)
