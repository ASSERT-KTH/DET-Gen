# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_2265 as module_0
import builtins as module_1


#@pytest.mark.xfail(strict=True)
def test_case_0():
    str_0 = "#pxYo.F0"
    var_0 = module_0.func(*str_0)
    assert var_0 == ".#"
#    module_0.func()


#@pytest.mark.xfail(strict=True)
#def test_case_1():
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_2():
    str_0 = "\x0c5Z6QgAmf["
    list_0 = [str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == ".\x0c.5.z.6.q.g.m.f.["
    var_1 = module_0.func(*list_0)
    assert var_1 == ".\x0c.5.z.6.q.g.m.f.["
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_3():
    str_0 = "^%yTT]$O(pGFl"
    list_0 = [str_0, str_0, str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == ".^.%.t.t.].$.(.p.g.f.l"
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_4():
    str_0 = "Jw^ uH8"
    list_0 = [str_0, str_0, str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == ".j.w.^. .h.8"
#    module_1.object(**var_0)


#@pytest.mark.xfail(strict=True)
def test_case_5():
    str_0 = "LeP8Hm\\A'NUz,sA%)l^"
    list_0 = [str_0, str_0, str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == ".l.p.8.h.m.\\.'.n.z.,.s.%.).l.^"
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_6():
    str_0 = "I&`rZ2rQk84FQJK<u^=."
    list_0 = [str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == ".&.`.r.z.2.r.q.k.8.4.f.q.j.k.<.^.=.."
    var_1 = module_0.func(*list_0)
    assert var_1 == ".&.`.r.z.2.r.q.k.8.4.f.q.j.k.<.^.=.."
#    module_0.func()
