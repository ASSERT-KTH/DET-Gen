# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_2158 as module_0
import builtins as module_1


#@pytest.mark.xfail(strict=True)
#def test_case_0():
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_1():
    str_0 = "48\nZvRH\rx/,"
    list_0 = [str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == "01:10"
    object_0 = module_1.object()
#    module_0.func(*object_0)


def test_case_2():
    str_0 = "RqI\x0b\x0csKpH o\\H&q`h%7\x0b"
    list_0 = [str_0, str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == "10:01"


#@pytest.mark.xfail(strict=True)
def test_case_3():
    str_0 = "38\nZvRH\rx/,"
    list_0 = [str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == "15:51"
    object_0 = module_1.object()
#    module_1.object(*str_0)


#@pytest.mark.xfail(strict=True)
def test_case_4():
    str_0 = "1ZvRH\rx/,"
    list_0 = [str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == "20:02"
    object_0 = module_1.object()
#    module_0.func()
