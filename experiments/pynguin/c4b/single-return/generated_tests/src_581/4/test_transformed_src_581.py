# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_581 as module_0


#@pytest.mark.xfail(strict=True)
def test_case_0():
    dict_0 = {}
    list_0 = [dict_0, dict_0, dict_0]
    list_1 = [list_0, list_0, list_0, list_0]
    list_2 = [dict_0, dict_0, dict_0, list_1, list_0]
    var_0 = module_0.func(*list_2)
    set_0 = {var_0}
    list_3 = [set_0, dict_0, dict_0]
    list_4 = [list_3, list_1]
#    module_0.func(*list_4)


#@pytest.mark.xfail(strict=True)
def test_case_1():
    bool_0 = False
    tuple_0 = (bool_0,)
    list_0 = [tuple_0, tuple_0]
#    module_0.func(*list_0)


#@pytest.mark.xfail(strict=True)
def test_case_2():
    list_0 = []
#    module_0.func(*list_0)


#@pytest.mark.xfail(strict=True)
def test_case_3():
    str_0 = "_0\\aK[H5*#\x0cNta:LBoT4"
    dict_0 = {str_0: str_0}
    list_0 = [dict_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == "_0\\ak[h5*#\x0cnta:lbot4"
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_4():
    str_0 = "_0\\aK[H5*#\x0cNta:LBoT4"
    list_0 = [str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == "_0\\aK[H5*#\x0cNta:LBoT4"
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_5():
    str_0 = "l3~h6UT(Q"
    dict_0 = {str_0: str_0}
    list_0 = [dict_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == "L3~H6UT(Q"
#    module_0.func()
