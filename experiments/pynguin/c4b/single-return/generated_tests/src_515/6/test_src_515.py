# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_515 as module_0
import builtins as module_1


@pytest.mark.xfail(strict=True)
def test_case_0():
    bool_0 = True
    list_0 = [bool_0]
    list_1 = [list_0]
    module_0.func(*list_1)


@pytest.mark.xfail(strict=True)
def test_case_1():
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_2():
    str_0 = "S\x0c5n\x0bnf\rToe3zTZX"
    list_0 = [str_0, str_0, str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == ".s.\x0c.5.n.\x0b.n.f.\r.t.3.z.t.z.x"
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_3():
    str_0 = "S\x0cn\x0bnfToe3KuTZX"
    list_0 = [str_0, str_0, str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == ".s.\x0c.n.\x0b.n.f.t.3.k.t.z.x"
    var_1 = module_0.func(*list_0)
    assert var_1 == ".s.\x0c.n.\x0b.n.f.t.3.k.t.z.x"
    object_0 = module_1.object()
    object_1 = module_1.object()
    var_2 = module_0.func(*var_1)
    assert var_2 == ".."
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_4():
    str_0 = "S\x0c5H\x0bff\rT$e3zTiZX"
    list_0 = [str_0, str_0, str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == ".s.\x0c.5.h.\x0b.f.f.\r.t.$.3.z.t.z.x"
    var_1 = module_0.func(*list_0)
    assert var_1 == ".s.\x0c.5.h.\x0b.f.f.\r.t.$.3.z.t.z.x"
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_5():
    str_0 = "Wa\x0csr"
    list_0 = [str_0, str_0, str_0, str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == ".w.\x0c.s.r"
    var_1 = module_0.func(*list_0)
    assert var_1 == ".w.\x0c.s.r"
    var_2 = module_0.func(*var_1)
    assert var_2 == ".."
    object_0 = module_1.object()
    object_1 = module_1.object()
    list_1 = [object_1, object_1]
    module_0.func(*list_1)


@pytest.mark.xfail(strict=True)
def test_case_6():
    str_0 = ""
    list_0 = [str_0, str_0, str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == ""
    module_0.func(*str_0)


@pytest.mark.xfail(strict=True)
def test_case_7():
    str_0 = "]XczBO|R;-Qc[v(Wy\x0b"
    list_0 = [str_0, str_0, str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == ".].x.c.z.b.|.r.;.-.q.c.[.v.(.w.\x0b"
    var_1 = module_0.func(*list_0)
    assert var_1 == ".].x.c.z.b.|.r.;.-.q.c.[.v.(.w.\x0b"
    object_0 = module_1.object()
    var_2 = module_0.func(*var_1)
    assert var_2 == ".."
    object_1 = module_1.object()
    list_1 = [object_1, object_1]
    module_0.func(*list_1)
