# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_525 as module_0
import builtins as module_1


def test_case_0():
    str_0 = "hX?HweG%;f3>UG\n_AS\x0b"
    var_0 = module_0.func(*str_0)
    assert var_0 == ".h"


#@pytest.mark.xfail(strict=True)
#def test_case_1():
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_2():
    str_0 = "I!"
    list_0 = [str_0, str_0, str_0, str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == ".!"
    tuple_0 = (var_0, var_0, var_0, list_0)
    list_1 = [tuple_0]
#    module_0.func(*list_1)


#@pytest.mark.xfail(strict=True)
def test_case_3():
    str_0 = 'O<mq&\rX"#nRH/'
    list_0 = [str_0, str_0, str_0, str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == '.<.m.q.&.\r.x.".#.n.r.h./'
    tuple_0 = (var_0, var_0, var_0, list_0)
    list_1 = [tuple_0]
#    module_0.func(*list_1)


#@pytest.mark.xfail(strict=True)
def test_case_4():
    str_0 = "hX?HweG%;f3>UG\n_AS\x0b"
    list_0 = [str_0, str_0, str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == ".h.x.?.h.w.g.%.;.f.3.>.g.\n._.s.\x0b"
    var_1 = module_0.func(*str_0)
    assert var_1 == ".h"
#    module_1.object(*str_0)


#@pytest.mark.xfail(strict=True)
def test_case_5():
    str_0 = "`yC,kG'>l>abJi)~Q"
    list_0 = [str_0, str_0, str_0, str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == ".`.c.,.k.g.'.>.l.>.b.j.).~.q"
    tuple_0 = (var_0, var_0, var_0, list_0)
    list_1 = [tuple_0]
#    module_0.func(*list_1)
