# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_2342 as module_0
import builtins as module_1


def test_case_0():
    str_0 = "_V;BV)lk"
    var_0 = module_0.func(*str_0)


#@pytest.mark.xfail(strict=True)
def test_case_1():
    list_0 = []
    var_0 = module_1.object(*list_0)
    list_1 = [list_0, list_0, list_0, list_0]
    var_1 = module_0.func(*list_1)
#    module_0.func(*list_0)


#@pytest.mark.xfail(strict=True)
#def test_case_2():
#    module_0.func()


def test_case_3():
    str_0 = "_V;BV)lk"
    list_0 = [str_0, str_0]
    var_0 = module_0.func(*list_0)


def test_case_4():
    str_0 = "0\x0cq{;()w6"
    var_0 = module_0.func(*str_0)


def test_case_5():
    str_0 = "3~1|90euJi"
    list_0 = [str_0, str_0]
    var_0 = module_0.func(*list_0)


#@pytest.mark.xfail(strict=True)
def test_case_6():
    str_0 = "3g000eu0J000"
    list_0 = [str_0]
    var_0 = module_0.func(*list_0)
    var_1 = module_0.func(*list_0)
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_7():
    str_0 = "11111]=1100ec0l00"
    list_0 = [str_0, str_0, str_0]
    var_0 = module_0.func(*list_0)
    var_1 = module_0.func(*str_0)
    var_2 = module_0.func(*var_1)
#    module_1.object(**var_2)
