# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_252 as module_0
import builtins as module_1


def test_case_0():
    str_0 = "KQx~\rGQtJs$pF&DC8L7K"
    var_0 = module_0.func(*str_0)
    assert var_0 == 2


def test_case_1():
    str_0 = "I"
    var_0 = module_0.func(*str_0)
    assert var_0 == 1
    object_0 = module_1.object()


#@pytest.mark.xfail(strict=True)
def test_case_2():
    str_0 = ")c[MpT,+IE6"
    list_0 = [str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == 9
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_3():
    object_0 = module_1.object()
    str_0 = "h}(\\A"
    list_0 = [str_0, object_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == 5
    var_1 = module_0.func(*str_0)
    assert var_1 == 2
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_4():
    object_0 = module_1.object()
    str_0 = "Us"
    var_0 = module_0.func(*str_0)
    assert var_0 == 1
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_5():
    str_0 = "HTO.nYKR^9^(xQ}pg"
    list_0 = [str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == 12
#    module_0.func()
