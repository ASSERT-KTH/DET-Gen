# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_525 as module_0
import builtins as module_1


def test_case_0():
    str_0 = "`RK%V5L\rL&.cD"
    bytes_0 = b"3\x8c\xd0\xc7\xa4\x13TtW=\x88"
    list_0 = [str_0, bytes_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == ".`.r.k.%.v.5.l.\r.l.&...c.d"


#@pytest.mark.xfail(strict=True)
#def test_case_1():
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_2():
    str_0 = "D!8%KQ0a:"
    list_0 = [str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == ".d.!.8.%.k.q.0.:"
    none_type_0 = None
    list_1 = [none_type_0]
#    module_0.func(*list_1)


def test_case_3():
    str_0 = "`RO%V5L\rL&.cD"
    bytes_0 = b"3\x8c\xd0\xc7\xa4\x13TtW=\x88"
    list_0 = [str_0, bytes_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == ".`.r.%.v.5.l.\r.l.&...c.d"


def test_case_4():
    str_0 = "HLES8U&."
    bytes_0 = b'n\xc3.\x84\xf1H\xaaD\xdf\x07%a\x8e\xc2-"'
    list_0 = [str_0, bytes_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == ".h.l.s.8.&.."


#@pytest.mark.xfail(strict=True)
def test_case_5():
    str_0 = "&J+IE\r"
    list_0 = [str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == ".&.j.+.\r"
    var_1 = module_1.object()
    var_2 = module_0.func(*list_0)
    assert var_2 == ".&.j.+.\r"
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_6():
    str_0 = "RTY'n[{Wl*xPR5"
    list_0 = [str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == ".r.t.'.n.[.{.w.l.*.x.p.r.5"
#    module_0.func()
