# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_2398 as module_0


def test_case_0():
    str_0 = "QGTr.$e, }c[ /-mH\x0bH&"
    var_0 = module_0.func(*str_0)
    assert var_0 == ".q"


#@pytest.mark.xfail(strict=True)
#def test_case_1():
#    module_0.func()


def test_case_2():
    str_0 = "QGTr.$e, }c[ /-mH\x0bH&"
    list_0 = [str_0, str_0, str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == ".q.g.t.r...$.,. .}.c.[. ./.-.m.h.\x0b.h.&"


def test_case_3():
    str_0 = "'5sHCjOJ;2Rqv"
    list_0 = [str_0, str_0, str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == ".'.5.s.h.c.j.j.;.2.r.q.v"


def test_case_4():
    str_0 = "XQGU$"
    list_0 = [str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == ".x.q.g.$"


def test_case_5():
    str_0 = ")GTr.$e,%\\c[ /-mHi1&"
    list_0 = [str_0, str_0, str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == ".).g.t.r...$.,.%.\\.c.[. ./.-.m.h.1.&"


def test_case_6():
    str_0 = "SuXlZRYl%( \r "
    list_0 = [str_0, str_0, str_0, str_0, str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == ".s.x.l.z.r.l.%.(. .\r. "


def test_case_7():
    str_0 = "RbAg"
    list_0 = [str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == ".r.b.g"
