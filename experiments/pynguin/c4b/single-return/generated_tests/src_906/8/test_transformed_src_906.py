# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_906 as module_0
import builtins as module_1


#@pytest.mark.xfail(strict=True)
def test_case_0():
    str_0 = "ZwHt7Z)I"
    var_0 = module_0.func(*str_0)
    assert var_0 == ".z"
#    module_0.func()


#@pytest.mark.xfail(strict=True)
#def test_case_1():
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_2():
    str_0 = "p\x0c\t1SkF%HXJbaKru6%["
    list_0 = [str_0, str_0, str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == ".p.\x0c.\t.1.s.k.f.%.h.x.j.b.k.r.6.%.["
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_3():
    str_0 = "ZwHt7Z)I"
    list_0 = [str_0, str_0, str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == ".z.w.h.t.7.z.)"
    str_1 = "1/\x0cZF\tfh75"
    var_1 = module_0.func(*str_1)
    assert var_1 == ".1"
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_4():
    str_0 = "O"
    list_0 = [str_0, str_0, str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == ""
    str_1 = "1/\x0cZF\tfh75"
    var_1 = module_0.func(*str_1)
    assert var_1 == ".1"
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_5():
    str_0 = "RD2o1w\n\t/[`>=2ld "
    list_0 = [str_0, str_0, str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == ".r.d.2.1.w.\n.\t./.[.`.>.=.2.l.d. "
    list_1 = [var_0]
    var_1 = module_0.func(*list_1)
    assert var_1 == "...r...d...2...1...w...\n...\t.../...[...`...>...=...2...l...d... "
    var_2 = module_0.func(*var_0)
    assert var_2 == ".."
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_6():
    str_0 = "qdUK\t[k4e#\r}%y|X"
    list_0 = [str_0, str_0, str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == ".q.d.k.\t.[.k.4.#.\r.}.%.|.x"
    list_1 = [var_0, str_0]
    var_1 = module_0.func(*list_1)
    assert var_1 == "...q...d...k...\t...[...k...4...#...\r...}...%...|...x"
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_7():
    str_0 = "p\x0c\t1SxF%HXJbYKru6%["
    list_0 = [str_0, str_0, str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == ".p.\x0c.\t.1.s.x.f.%.h.x.j.b.k.r.6.%.["
    var_1 = module_0.func(*var_0)
    assert var_1 == ".."
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_8():
    str_0 = "p\x0c\t1SkF%HXAJbaKru6%["
    list_0 = [str_0, str_0, str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == ".p.\x0c.\t.1.s.k.f.%.h.x.j.b.k.r.6.%.["
    list_1 = [var_0, var_0, str_0, var_0]
    var_1 = module_0.func(*list_1)
    assert (
        var_1
        == "...p...\x0c...\t...1...s...k...f...%...h...x...j...b...k...r...6...%...["
    )
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_9():
    str_0 = "bN_kU*:SNOkSuX-Pc*"
    list_0 = [str_0, str_0, str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == ".b.n._.k.*.:.s.n.k.s.x.-.p.c.*"
    list_1 = [var_0]
    var_1 = module_0.func(*list_1)
    assert var_1 == "...b...n..._...k...*...:...s...n...k...s...x...-...p...c...*"
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_10():
    str_0 = "p\x0c\t1SkF%HXibaKru6%["
    list_0 = [str_0, str_0, str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == ".p.\x0c.\t.1.s.k.f.%.h.x.b.k.r.6.%.["
    var_1 = module_1.object()
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_11():
    str_0 = "}h\np#e6(p0n X~\r~hE)`"
    list_0 = [str_0, str_0, str_0, str_0, str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == ".}.h.\n.p.#.6.(.p.0.n. .x.~.\r.~.h.).`"
    list_1 = [var_0, list_0, var_0]
    var_1 = module_0.func(*list_1)
    assert (
        var_1
        == "...}...h...\n...p...#...6...(...p...0...n... ...x...~...\r...~...h...)...`"
    )
#    module_0.func()
