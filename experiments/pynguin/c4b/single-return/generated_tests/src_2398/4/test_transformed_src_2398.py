# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_2398 as module_0
import builtins as module_1


def test_case_0():
    str_0 = 'cWaTN%"#OAXJ+&'
    var_0 = module_0.func(*str_0)
    assert var_0 == ".c"


#@pytest.mark.xfail(strict=True)
#def test_case_1():
#    module_0.func()


def test_case_2():
    str_0 = 'cWaTN%"#OAXJ+&'
    list_0 = [str_0, str_0, str_0, str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == '.c.w.t.n.%.".#.x.j.+.&'


#@pytest.mark.xfail(strict=True)
def test_case_3():
    str_0 = 'cWauN]a%"#OAXJ+&'
    list_0 = [str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == '.c.w.n.].%.".#.x.j.+.&'
#    module_1.object(*list_0)


#@pytest.mark.xfail(strict=True)
def test_case_4():
    str_0 = "!qV32;)D3Ne"
    list_0 = [str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == ".!.q.v.3.2.;.).d.3.n"
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_5():
    str_0 = 'cWaTN%"#OA=J+y7&'
    list_0 = [str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == '.c.w.t.n.%.".#.=.j.+.7.&'
#    module_1.object(*var_0)


#@pytest.mark.xfail(strict=True)
def test_case_6():
    str_0 = "cW'aTNi\"#OAXJ+&"
    list_0 = [str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == ".c.w.'.t.n.\".#.x.j.+.&"
#    module_0.func()
