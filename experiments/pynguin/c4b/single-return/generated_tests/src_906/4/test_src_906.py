# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_906 as module_0
import builtins as module_1


def test_case_0():
    str_0 = "O"
    var_0 = module_0.func(*str_0)
    assert var_0 == ""


@pytest.mark.xfail(strict=True)
def test_case_1():
    str_0 = "x/Re_6ihdKKbdX"
    var_0 = module_0.func(*str_0)
    assert var_0 == ".x"
    list_0 = [str_0]
    var_1 = module_0.func(*list_0)
    assert var_1 == ".x./.r._.6.h.d.k.k.b.d.x"
    module_0.func()


def test_case_2():
    str_0 = "y"
    var_0 = module_0.func(*str_0)
    assert var_0 == ""


@pytest.mark.xfail(strict=True)
def test_case_3():
    str_0 = "l\tZ?y'PpSibPu"
    list_0 = [str_0, str_0, str_0, str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == ".l.\t.z.?.'.p.p.s.b.p"
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_4():
    str_0 = "!\tZ?y'PpS\nibPsU"
    dict_0 = {str_0: str_0, str_0: str_0, str_0: str_0, str_0: str_0}
    var_0 = module_0.func(*dict_0)
    assert var_0 == ".!.\t.z.?.'.p.p.s.\n.b.p.s"
    module_1.object(**dict_0)


@pytest.mark.xfail(strict=True)
def test_case_5():
    str_0 = "QRpO\nSS-Ast-N!z"
    list_0 = [str_0, str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == ".q.r.p.\n.s.s.-.s.t.-.n.!.z"
    var_1 = module_0.func(*list_0)
    assert var_1 == ".q.r.p.\n.s.s.-.s.t.-.n.!.z"
    list_1 = []
    module_0.func(*list_1)


@pytest.mark.xfail(strict=True)
def test_case_6():
    str_0 = "lo%$bX7YP &"
    list_0 = [str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == ".l.%.$.b.x.7.p. .&"
    list_1 = [str_0, str_0]
    var_1 = module_0.func(*list_1)
    assert var_1 == ".l.%.$.b.x.7.p. .&"
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_7():
    str_0 = "!NZ?yKtpS|ibPsa"
    list_0 = [str_0, str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == ".!.n.z.?.k.t.p.s.|.b.p.s"
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_8():
    str_0 = "!NZ?yKtE'pS|ibPsa"
    dict_0 = {str_0: str_0, str_0: str_0}
    var_0 = module_0.func(*dict_0)
    assert var_0 == ".!.n.z.?.k.t.'.p.s.|.b.p.s"
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_9():
    str_0 = "\x0b\x0c?[hj.[c$IC5Dr,nbxw"
    dict_0 = {str_0: str_0, str_0: str_0}
    var_0 = module_0.func(*dict_0)
    assert var_0 == ".\x0b.\x0c.?.[.h.j...[.c.$.c.5.d.r.,.n.b.x.w"
    module_1.object(*var_0, **dict_0)
