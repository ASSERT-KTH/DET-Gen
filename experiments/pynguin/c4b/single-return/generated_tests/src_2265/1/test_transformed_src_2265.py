# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_2265 as module_0
import builtins as module_1


def test_case_0():
    str_0 = "Q"
    list_0 = [str_0, str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == ".q"


#@pytest.mark.xfail(strict=True)
#def test_case_1():
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_2():
    str_0 = "neuONq j+rX/|"
    var_0 = module_0.func(*str_0)
    assert var_0 == ".n"
    list_0 = [str_0, str_0, str_0, str_0]
    var_1 = module_0.func(*list_0)
    assert var_1 == ".n.n.q. .j.+.r.x./.|"
    list_1 = [var_0, var_0]
    var_2 = module_0.func(*list_1)
    assert var_2 == "...n"
    var_3 = module_0.func(*list_1)
    assert var_3 == "...n"
    list_2 = []
#    module_0.func(*list_2)


#@pytest.mark.xfail(strict=True)
def test_case_3():
    str_0 = "i"
    var_0 = module_0.func(*str_0)
    assert var_0 == ""
#    module_1.object(**var_0)


#@pytest.mark.xfail(strict=True)
def test_case_4():
    str_0 = "3'G\x0cYN#=wel32"
    list_0 = [str_0, str_0, str_0, str_0, str_0, str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == ".3.'.g.\x0c.n.#.=.w.l.3.2"
    object_0 = module_1.object()
#    module_1.object(*var_0)


#@pytest.mark.xfail(strict=True)
def test_case_5():
    str_0 = "Ah1\r54\n#S{"
    var_0 = module_0.func(*str_0)
    assert var_0 == ""
    var_1 = module_1.object()
#    module_0.func(*var_1)
