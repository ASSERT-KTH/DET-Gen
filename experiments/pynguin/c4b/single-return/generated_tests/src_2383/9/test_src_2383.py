# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_2383 as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    str_0 = "-J'wy7RK-&C%hw_pJFC"
    var_0 = module_0.func(*str_0)
    assert var_0 == ".-"
    list_0 = [str_0]
    var_1 = module_0.func(*list_0)
    assert var_1 == ".-.j.'.w.7.r.k.-.&.c.%.h.w._.p.j.f.c"
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_1():
    float_0 = 2447.448
    list_0 = [float_0]
    module_0.func(*list_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    str_0 = "AJf*g@AY1"
    list_0 = [str_0, str_0, str_0, str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == ".j.f.*.g.@.1"
    list_1 = []
    module_0.func(*list_1)


@pytest.mark.xfail(strict=True)
def test_case_3():
    str_0 = "8EL!$@[P#;pVnI*u5C"
    list_0 = [str_0, str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == ".8.l.!.$.@.[.p.#.;.p.v.n.*.5.c"
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_4():
    str_0 = ")Lx8b%L=h2o4@"
    list_0 = [str_0, str_0, str_0, str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == ".).l.x.8.b.%.l.=.h.2.4.@"
    var_1 = module_0.func(*list_0)
    assert var_1 == ".).l.x.8.b.%.l.=.h.2.4.@"
    module_0.func()
