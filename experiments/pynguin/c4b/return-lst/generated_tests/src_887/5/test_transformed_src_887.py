# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_887 as module_0


def test_case_0():
    int_0 = 7
    set_0 = {int_0, int_0, int_0, int_0, int_0}
    list_0 = [set_0, set_0, set_0]
    var_0 = module_0.func(*list_0)


#@pytest.mark.xfail(strict=True)
#def test_case_1():
#    module_0.func()


def test_case_2():
    int_0 = 4
    set_0 = {int_0, int_0, int_0, int_0, int_0}
    list_0 = [set_0, set_0, set_0]
    var_0 = module_0.func(*list_0)


def test_case_3():
    int_0 = -1514
    set_0 = {int_0, int_0}
    str_0 = '&"\nRT81\x0b<p=tw'
    list_0 = [set_0, set_0, str_0]
    var_0 = module_0.func(*list_0)


#@pytest.mark.xfail(strict=True)
def test_case_4():
    int_0 = 4
    list_0 = [int_0, int_0, int_0, int_0]
    list_1 = [list_0]
    var_0 = module_0.func(*list_1)
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_5():
    int_0 = 4
    list_0 = [int_0, int_0, int_0, int_0, int_0, int_0, int_0]
    list_1 = [list_0]
    var_0 = module_0.func(*list_1)
#    module_0.func()
