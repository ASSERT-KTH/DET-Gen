# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import builtins as module_0
import src_944 as module_1


def test_case_0():
    object_0 = module_0.object()
    set_0 = {object_0, object_0, object_0, object_0}
    list_0 = [set_0, object_0, set_0, set_0]
    var_0 = module_1.func(*list_0)
    assert var_0 == 0


#@pytest.mark.xfail(strict=True)
#def test_case_1():
#    module_1.func()


def test_case_2():
    str_0 = "\x0cepVddx"
    list_0 = [str_0, str_0, str_0]
    var_0 = module_1.func(*list_0)
    assert var_0 == 0


#@pytest.mark.xfail(strict=True)
def test_case_3():
    str_0 = "E#4Kp"
    list_0 = [str_0, str_0, str_0]
    var_0 = module_1.func(*list_0)
    assert var_0 == 0
    object_0 = module_0.object()
#    module_1.func()


#@pytest.mark.xfail(strict=True)
def test_case_4():
    str_0 = "#K4Kp"
    list_0 = [str_0, str_0]
    var_0 = module_1.func(*list_0)
    assert var_0 == 1
#    module_1.func()


#@pytest.mark.xfail(strict=True)
def test_case_5():
    str_0 = "VVK"
    list_0 = [str_0, str_0]
    var_0 = module_1.func(*list_0)
    assert var_0 == 1
#    module_1.func()


#@pytest.mark.xfail(strict=True)
def test_case_6():
    str_0 = "eVKlK"
    list_0 = [str_0, str_0]
    var_0 = module_1.func(*list_0)
    assert var_0 == 2
#    module_1.func()


#@pytest.mark.xfail(strict=True)
def test_case_7():
    str_0 = "VVlK"
    list_0 = [str_0, str_0]
    var_0 = module_1.func(*list_0)
    assert var_0 == 1
#    module_1.func()


#@pytest.mark.xfail(strict=True)
def test_case_8():
    str_0 = "'VV"
    list_0 = [str_0, str_0]
    var_0 = module_1.func(*list_0)
    assert var_0 == 1
#    module_1.func()
