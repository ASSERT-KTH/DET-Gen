# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_2245 as module_0
import builtins as module_1


#@pytest.mark.xfail(strict=True)
#def test_case_0():
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_1():
    str_0 = ". P\to)"
    var_0 = module_0.func(*str_0)
    assert var_0 == "."
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_2():
    str_0 = "iD?Llcl[)g"
    list_0 = [str_0, str_0, str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == "iD?Llcl[)g"
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_3():
    str_0 = ". P\to)"
    var_0 = module_0.func(*str_0)
    assert var_0 == "."
    list_0 = [str_0, str_0, str_0]
    var_1 = module_0.func(*list_0)
    assert var_1 == ". P\to)"
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_4():
    str_0 = "iD?Llcl[)g"
    var_0 = module_0.func(*str_0)
    assert var_0 == "I"
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_5():
    object_0 = module_1.object()
    str_0 = "|\r:h6^"
    list_0 = [str_0, str_0, str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == "|\r:h6^"
    set_0 = module_0.func(*list_0)
    assert set_0 == "|\r:h6^"
    var_1 = module_0.func(*var_0)
    assert var_1 == "|"
    var_2 = module_0.func(*set_0)
    assert var_2 == "|"
#    module_0.func()
