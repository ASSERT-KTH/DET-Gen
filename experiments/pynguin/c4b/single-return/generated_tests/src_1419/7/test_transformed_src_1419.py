# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_1419 as module_0
import builtins as module_1


#@pytest.mark.xfail(strict=True)
def test_case_0():
    dict_0 = {}
    list_0 = [dict_0, dict_0, dict_0, dict_0]
#    module_0.func(*list_0)


#@pytest.mark.xfail(strict=True)
def test_case_1():
    str_0 = "r|{SP`'5{"
    list_0 = [str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == "R|{sp`'5{"
    list_1 = [var_0, var_0, var_0]
    var_1 = module_0.func(*list_1)
    assert var_1 == "R|{sp`'5{"
#    module_0.func()


#@pytest.mark.xfail(strict=True)
#def test_case_2():
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_3():
    str_0 = "r|{P`'5{"
    list_0 = [str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == "R|{p`'5{"
    list_1 = [var_0, var_0, var_0]
    var_1 = module_0.func(*list_1)
    assert var_1 == "R|{p`'5{"
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_4():
    str_0 = "r|{P`'5{"
    list_0 = [str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == "R|{p`'5{"
    object_0 = module_1.object()
    var_1 = module_0.func(*var_0)
    assert var_1 == "r"
#    module_0.func()
