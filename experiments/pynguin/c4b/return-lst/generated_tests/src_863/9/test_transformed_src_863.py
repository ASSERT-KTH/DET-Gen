# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_863 as module_0


def test_case_0():
    bool_0 = False
    list_0 = [bool_0]
    var_0 = module_0.func(*list_0)


def test_case_1():
    bool_0 = True
    list_0 = [bool_0]
    var_0 = module_0.func(*list_0)


#@pytest.mark.xfail(strict=True)
#def test_case_2():
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_3():
    str_0 = "7A"
    var_0 = module_0.func(*str_0)
#    module_0.func()


def test_case_4():
    int_0 = 417
    list_0 = [int_0, int_0, int_0]
    var_0 = module_0.func(*list_0)


#@pytest.mark.xfail(strict=True)
def test_case_5():
    int_0 = -2726
    list_0 = [int_0, int_0]
    var_0 = module_0.func(*list_0)
#    module_0.func()


def test_case_6():
    int_0 = 474
    list_0 = [int_0, int_0]
    var_0 = module_0.func(*list_0)
    list_1 = [int_0, int_0, int_0]
    var_1 = module_0.func(*list_1)
