# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_1529 as module_0
import builtins as module_1


def test_case_0():
    str_0 = "aU-<J=A3iAh"
    list_0 = [str_0, str_0, str_0]
    var_0 = module_0.func(*list_0)


#@pytest.mark.xfail(strict=True)
#def test_case_1():
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_2():
    str_0 = "aU-<J=A3iAh"
    list_0 = [str_0, str_0, str_0]
    bool_0 = True
    list_1 = [list_0, str_0, str_0, bool_0]
#    module_0.func(*list_1)


def test_case_3():
    str_0 = "aU-<J=A3iAh"
    var_0 = module_0.func(*str_0)
    list_0 = [str_0, str_0, str_0]
    var_1 = module_0.func(*list_0)


#@pytest.mark.xfail(strict=True)
def test_case_4():
    str_0 = "aU-<J=A3iAh"
    var_0 = module_0.func(*str_0)
    list_0 = module_0.func(*var_0)
#    module_1.object(*list_0)


#@pytest.mark.xfail(strict=True)
def test_case_5():
    str_0 = "O79')_N%QL"
    list_0 = [str_0]
    var_0 = module_0.func(*list_0)
    str_1 = "aU-<J=A3iAh"
    list_1 = [str_1, str_1, str_1]
    var_1 = module_0.func(*list_1)
    list_2 = [list_1, str_1, str_1, var_1]
#    module_0.func(*list_2)


def test_case_6():
    str_0 = "#9-(J=A3iAh"
    list_0 = [str_0, str_0]
    var_0 = module_0.func(*list_0)
    var_1 = module_0.func(*str_0)
    var_2 = module_0.func(*var_1)


def test_case_7():
    str_0 = "pF"
    list_0 = [str_0, str_0, str_0, str_0]
    var_0 = module_0.func(*list_0)
    str_1 = "aU-<J=A3iAh"
    list_1 = [str_1, str_1]
    var_1 = module_0.func(*list_1)
    var_2 = module_0.func(*str_1)
    var_3 = module_0.func(*var_2)
