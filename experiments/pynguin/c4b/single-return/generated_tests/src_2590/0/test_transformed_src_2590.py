# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_2590 as module_0
import builtins as module_1


#@pytest.mark.xfail(strict=True)
def test_case_0():
    bool_0 = True
    list_0 = [bool_0, bool_0, bool_0, bool_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == "7"
#    module_0.func()


#@pytest.mark.xfail(strict=True)
#def test_case_1():
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_2():
    bool_0 = True
    list_0 = [bool_0, bool_0, bool_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == "7"
    list_1 = [var_0, bool_0]
    var_1 = module_0.func(*list_1)
    assert var_1 == "711"
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_3():
    bool_0 = False
    list_0 = [bool_0, bool_0, bool_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == ""
    list_1 = []
#    module_0.func(*list_1)


#@pytest.mark.xfail(strict=True)
def test_case_4():
    str_0 = "4jZ:="
    var_0 = module_0.func(*str_0)
    assert var_0 == "11"
#    module_1.object(*var_0)