# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_2087 as module_0
import builtins as module_1


def test_case_0():
    set_0 = set()
    list_0 = [set_0]
    var_0 = module_0.func(*list_0)


#@pytest.mark.xfail(strict=True)
#def test_case_1():
#    module_0.func()


def test_case_2():
    set_0 = set()
    list_0 = [set_0, set_0, set_0, set_0, set_0, set_0]
    list_1 = [list_0]
    var_0 = module_0.func(*list_1)


def test_case_3():
    set_0 = set()
    list_0 = [set_0, set_0]
    var_0 = module_0.func(*list_0)
    var_1 = module_0.func(*var_0)


#@pytest.mark.xfail(strict=True)
def test_case_4():
    set_0 = set()
    tuple_0 = (set_0,)
    list_0 = [set_0, tuple_0, tuple_0]
    var_0 = module_0.func(*list_0)
    list_1 = [set_0, set_0, set_0, list_0, set_0, set_0, set_0, set_0]
    var_1 = module_0.func(*list_1)
    list_2 = [list_1, var_1]
    var_2 = module_0.func(*var_1)
    var_3 = module_0.func(*list_2)
#    module_1.object(**var_0)


def test_case_5():
    set_0 = set()
    list_0 = [set_0, set_0, set_0, set_0, set_0, set_0, set_0]
    list_1 = [list_0, set_0]
    var_0 = module_0.func(*list_1)
