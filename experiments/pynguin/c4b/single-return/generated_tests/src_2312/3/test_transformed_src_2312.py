# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_2312 as module_0
import builtins as module_1


def test_case_0():
    tuple_0 = ()
    list_0 = [tuple_0, tuple_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == ""
    tuple_1 = (var_0,)
    list_1 = [tuple_1]
    var_1 = module_0.func(*list_1)
    assert var_1 == "."
    var_2 = module_0.func(*tuple_1)
    assert var_2 == ""


#@pytest.mark.xfail(strict=True)
def test_case_1():
    set_0 = set()
#    module_0.func(*set_0)


#@pytest.mark.xfail(strict=True)
def test_case_2():
    tuple_0 = ()
    list_0 = [tuple_0, tuple_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == ""
    tuple_1 = (var_0,)
    list_1 = [tuple_1]
    var_1 = module_0.func(*list_1)
    assert var_1 == "."
    var_2 = module_1.object()
    str_0 = "$K\\c)7%~<yX"
    list_2 = [str_0, var_0, list_0, var_2]
    var_3 = module_0.func(*list_2)
    assert var_3 == ".$.k.\\.c.).7.%.~.<.x"
#    module_0.func()
