# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_189 as module_0
import builtins as module_1


def test_case_0():
    str_0 = "+G;%Mp8a&U "
    var_0 = module_0.func(*str_0)
    assert var_0 == 0


#@pytest.mark.xfail(strict=True)
#def test_case_1():
#    module_0.func()


def test_case_2():
    str_0 = ")VV\\U eGw(.U"
    list_0 = [str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == 1
    object_0 = module_1.object()


#@pytest.mark.xfail(strict=True)
def test_case_3():
    str_0 = "+`-1KK1"
    list_0 = [str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == 1
    str_1 = "q*2!vv 0K"
    list_1 = [str_1, str_1]
    var_1 = module_0.func(*list_1)
    assert var_1 == 0
#    module_1.object(*str_0, **var_1)
