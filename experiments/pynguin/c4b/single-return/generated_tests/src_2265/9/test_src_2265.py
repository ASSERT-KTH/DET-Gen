# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_2265 as module_0
import builtins as module_1


def test_case_0():
    str_0 = "|J1l.~Wn|4dFJ`\ndO"
    var_0 = module_0.func(*str_0)
    assert var_0 == ".|"


@pytest.mark.xfail(strict=True)
def test_case_1():
    module_0.func()


def test_case_2():
    str_0 = "|J1l.~Wn|4dFJ`\ndO"
    list_0 = [str_0, str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == ".|.j.1.l...~.w.n.|.4.d.f.j.`.\n.d"


@pytest.mark.xfail(strict=True)
def test_case_3():
    str_0 = "OfDUQKS\x0cX2&/zqo\x0c\n"
    list_0 = [str_0, str_0]
    var_0 = module_0.func(*str_0)
    assert var_0 == ""
    var_1 = module_0.func(*list_0)
    assert var_1 == ".f.d.q.k.s.\x0c.x.2.&./.z.q.\x0c.\n"
    module_1.object(*var_1)


@pytest.mark.xfail(strict=True)
def test_case_4():
    str_0 = "2ER`*E|zWWRX"
    list_0 = [str_0, str_0, str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == ".2.r.`.*.|.z.w.w.r.x"
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_5():
    str_0 = "|J1l.~W|dFaIJ`\nO"
    list_0 = [str_0, str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == ".|.j.1.l...~.w.|.d.f.j.`.\n"
    var_1 = module_1.object()
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_6():
    str_0 = "y7{;om7$"
    list_0 = [str_0, str_0]
    var_0 = module_0.func(*str_0)
    assert var_0 == ""
    var_1 = module_0.func(*list_0)
    assert var_1 == ".7.{.;.m.7.$"
    module_1.object(*var_1)
