# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_1937 as module_0
import builtins as module_1


#@pytest.mark.xfail(strict=True)
def test_case_0():
    str_0 = "w@9KtC?{N%dv"
    var_0 = module_0.func(*str_0)
    assert var_0 == "W"
    var_1 = module_0.func(*var_0)
    assert var_1 == "w"
    var_2 = module_1.object()
    var_3 = module_0.func(*str_0)
    assert var_3 == "W"
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_1():
    str_0 = '%{Sl>atFq&"'
    list_0 = [str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == '%{Sl>atFq&"'
#    module_0.func()


#@pytest.mark.xfail(strict=True)
#def test_case_2():
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_3():
    str_0 = "0Y"
    list_0 = [str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == "0Y"
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_4():
    str_0 = "mY"
    list_0 = [str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == "My"
    var_1 = module_0.func(*str_0)
    assert var_1 == "M"
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_5():
    str_0 = "CY"
    list_0 = [str_0]
    var_0 = module_1.object()
    var_1 = module_0.func(*str_0)
    assert var_1 == "c"
    var_2 = module_0.func(*list_0)
    assert var_2 == "cy"
#    module_1.object(**var_1)
