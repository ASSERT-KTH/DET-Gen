# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_1018 as module_0
import builtins as module_1


def test_case_0():
    str_0 = "p\tGb"
    var_0 = module_0.func(*str_0)
    assert var_0 == 9


#@pytest.mark.xfail(strict=True)
#def test_case_1():
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_2():
    str_0 = "[3y2d1T#TE}$e\nJ"
    list_0 = [str_0, str_0, str_0, str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == 2653047
#    module_1.object(*var_0)


#@pytest.mark.xfail(strict=True)
def test_case_3():
    str_0 = "9v"
    list_0 = [str_0, str_0, str_0, str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == 99
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_4():
    str_0 = "329"
    list_0 = [str_0, str_0, str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == 161
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_5():
    str_0 = "32dL@1T#T}$e\nJr"
    list_0 = [str_0, str_0, str_0, str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == 1645487
    var_1 = module_0.func(*str_0)
    assert var_1 == 3
#    module_0.func()
