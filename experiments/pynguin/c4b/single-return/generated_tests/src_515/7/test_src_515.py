# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_515 as module_0
import builtins as module_1


def test_case_0():
    str_0 = "1^xR!`BM="
    var_0 = module_0.func(*str_0)
    assert var_0 == ".1"


@pytest.mark.xfail(strict=True)
def test_case_1():
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_2():
    set_0 = set()
    list_0 = [set_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == ""
    module_0.func()


def test_case_3():
    str_0 = "1^WxR!`B\nM="
    list_0 = [str_0, str_0, str_0, str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == ".1.^.w.x.r.!.`.b.\n.m.="


@pytest.mark.xfail(strict=True)
def test_case_4():
    str_0 = "u"
    bool_0 = True
    list_0 = [str_0, bool_0, str_0, str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == ""
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_5():
    str_0 = "iVF%Y**Bk-\t&{eyf"
    var_0 = module_0.func(*str_0)
    assert var_0 == ""
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_6():
    str_0 = "Oi\teh\nVH-q\\C"
    var_0 = module_0.func(*str_0)
    assert var_0 == ""
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_7():
    str_0 = "A.\x0cCctrkt"
    var_0 = module_0.func(*str_0)
    assert var_0 == ""
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_8():
    str_0 = "Yt'j\tpd\x0b"
    var_0 = module_0.func(*str_0)
    assert var_0 == ""
    module_1.object(*var_0, **var_0)


@pytest.mark.xfail(strict=True)
def test_case_9():
    str_0 = "e"
    list_0 = [str_0, str_0, str_0, str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == ""
    module_0.func()
