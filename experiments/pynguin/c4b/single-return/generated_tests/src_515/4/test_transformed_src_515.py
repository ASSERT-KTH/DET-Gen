# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_515 as module_0
import builtins as module_1


#@pytest.mark.xfail(strict=True)
def test_case_0():
    str_0 = "YBc\nfm`a"
    var_0 = module_0.func(*str_0)
    assert var_0 == ""
    var_1 = module_0.func(*str_0)
    assert var_1 == ""
#    module_0.func()


#@pytest.mark.xfail(strict=True)
#def test_case_1():
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_2():
    str_0 = "YBc\nfm`a"
    list_0 = [str_0, str_0, str_0, str_0, str_0, str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == ".b.c.\n.f.m.`"
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_3():
    str_0 = "YBc\nfm`a"
    list_0 = [str_0, str_0, str_0, str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == ".b.c.\n.f.m.`"
    var_1 = module_0.func(*var_0)
    assert var_1 == ".."
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_4():
    str_0 = "$1uPI-/hE!"
    list_0 = [str_0, str_0, str_0, str_0, str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == ".$.1.p.-./.h.!"
    var_1 = module_1.object()
    str_1 = ""
    list_1 = [var_1, str_0, str_1, var_0]
#    module_0.func(*list_1)


#@pytest.mark.xfail(strict=True)
def test_case_5():
    str_0 = "2O]vyI"
    list_0 = [str_0, str_0, str_0, str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == ".2.].v"
#    module_0.func()
