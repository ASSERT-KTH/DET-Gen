# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_592 as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    bytes_0 = b"a\x90hvFi\xea\x02"
    list_0 = [bytes_0, bytes_0, bytes_0]
    module_0.func(*list_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_2():
    str_0 = "8H7+fK"
    list_0 = [str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == ".8.h.7.+.f.k"
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_3():
    str_0 = "5mSfH%?tAhXYMBcZ#"
    list_0 = [str_0, str_0, str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == ".5.m.s.f.h.%.?.t.h.x.m.b.c.z.#"
    var_1 = module_0.func(*str_0)
    assert var_1 == ".5"
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_4():
    str_0 = "U$1pFN\n6gw\nur1=8"
    list_0 = [str_0, str_0, str_0, str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == ".$.1.p.f.n.\n.6.g.w.\n.r.1.=.8"
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_5():
    str_0 = "o"
    list_0 = [str_0, str_0, str_0, str_0, str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == ""
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_6():
    str_0 = "5mSfH%?tAhXEYMBcZ#"
    list_0 = [str_0, str_0, str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == ".5.m.s.f.h.%.?.t.h.x.m.b.c.z.#"
    var_1 = module_0.func(*str_0)
    assert var_1 == ".5"
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_7():
    str_0 = "5mSfH%?tA%XEIMBcZ#"
    list_0 = [str_0, str_0, str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == ".5.m.s.f.h.%.?.t.%.x.m.b.c.z.#"
    var_1 = module_0.func(*str_0)
    assert var_1 == ".5"
    module_0.func()
