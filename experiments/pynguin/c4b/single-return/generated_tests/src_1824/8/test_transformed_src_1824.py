# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_1824 as module_0
import builtins as module_1


#@pytest.mark.xfail(strict=True)
def test_case_0():
    list_0 = []
    list_1 = [list_0, list_0]
    var_0 = module_0.func(*list_1)
    assert var_0 == "NO"
#    module_0.func(*var_0)


#@pytest.mark.xfail(strict=True)
def test_case_1():
    list_0 = []
    list_1 = [list_0, list_0]
    var_0 = module_0.func(*list_1)
    assert var_0 == "NO"
    object_0 = module_1.object()
#    module_0.func()


#@pytest.mark.xfail(strict=True)
#def test_case_2():
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_3():
    bool_0 = False
    list_0 = [bool_0, bool_0]
    list_1 = [list_0]
    var_0 = module_0.func(*list_1)
    assert var_0 == "NO"
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_4():
    bool_0 = True
    list_0 = [bool_0, bool_0]
    list_1 = [list_0, list_0, list_0]
    var_0 = module_0.func(*list_1)
    assert var_0 == "NO"
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_5():
    bool_0 = True
    list_0 = [bool_0, bool_0, bool_0, bool_0, bool_0, bool_0, bool_0]
    list_1 = [list_0, list_0, list_0]
    var_0 = module_0.func(*list_1)
    assert var_0 == "YES"
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_6():
    bool_0 = False
    list_0 = [bool_0, bool_0, bool_0, bool_0, bool_0, bool_0, bool_0]
    list_1 = [list_0]
    var_0 = module_0.func(*list_1)
    assert var_0 == "YES"
#    module_1.object(**var_0)
