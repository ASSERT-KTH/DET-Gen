# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_194 as module_0
import builtins as module_1


#@pytest.mark.xfail(strict=True)
def test_case_0():
    str_0 = "ga\x0c\n~"
    list_0 = [str_0, str_0, str_0, str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == "ga\x0c\n~"
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_1():
    dict_0 = {}
    list_0 = [dict_0, dict_0, dict_0, dict_0]
#    module_0.func(*list_0)


#@pytest.mark.xfail(strict=True)
#def test_case_2():
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_3():
    str_0 = "U,4=l\ns~sE>^FDDjYIX6"
    var_0 = module_0.func(*str_0)
    assert var_0 == "U"
    var_1 = module_1.object()
#    module_0.func(*var_1)
