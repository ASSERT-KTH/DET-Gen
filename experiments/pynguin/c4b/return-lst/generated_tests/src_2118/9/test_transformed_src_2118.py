# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_2118 as module_0
import builtins as module_1


def test_case_0():
    int_0 = 1683
    list_0 = [int_0]
    var_0 = module_0.func(*list_0)


def test_case_1():
    int_0 = 1638
    list_0 = [int_0]
    var_0 = module_0.func(*list_0)


#@pytest.mark.xfail(strict=True)
#def test_case_2():
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_3():
    bool_0 = False
    list_0 = [bool_0, bool_0, bool_0, bool_0]
    var_0 = module_0.func(*list_0)
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_4():
    bytes_0 = b"J[v*6\x95\xdc\xfa\xfa\xd9\xbf\xa4\x11eD"
    var_0 = module_0.func(*bytes_0)
#    module_1.object(**var_0)
