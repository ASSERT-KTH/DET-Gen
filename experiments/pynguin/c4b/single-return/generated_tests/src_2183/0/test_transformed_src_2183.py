# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_2183 as module_0
import builtins as module_1


#@pytest.mark.xfail(strict=True)
def test_case_0():
    bool_0 = True
    list_0 = [bool_0, bool_0, bool_0, bool_0]
#    module_0.func(*list_0)


#@pytest.mark.xfail(strict=True)
#def test_case_1():
#    module_0.func()


def test_case_2():
    bool_0 = False
    list_0 = [bool_0, bool_0, bool_0, bool_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == "YES"


def test_case_3():
    str_0 = "73"
    list_0 = [str_0, str_0, str_0, str_0, str_0, str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == "NO"


#@pytest.mark.xfail(strict=True)
def test_case_4():
    str_0 = "43"
    list_0 = [str_0, str_0, str_0, str_0, str_0, str_0, str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == "NO"
    bool_0 = False
    list_1 = [bool_0, bool_0, bool_0, bool_0, bool_0, bool_0]
    var_1 = module_0.func(*list_1)
    assert var_1 == "YES"
#    module_1.object(**var_1)


#@pytest.mark.xfail(strict=True)
def test_case_5():
    str_0 = "41"
    list_0 = [str_0, str_0, str_0, str_0, str_0, str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == "NO"
    var_1 = module_0.func(*str_0)
    assert var_1 == "NO"
    bool_0 = False
    list_1 = [bool_0, bool_0, bool_0, bool_0, bool_0, bool_0]
    object_0 = module_1.object()
    var_2 = module_0.func(*list_1)
    assert var_2 == "YES"
    bool_1 = True
    list_2 = [bool_1, str_0, bool_1, var_0]
    var_3 = module_0.func(*list_2)
    assert var_3 == "NO"
#    module_1.object(**var_3)