# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_906 as module_0
import builtins as module_1


def test_case_0():
    str_0 = "\x0cQdUdBaQdE?nj_K"
    list_0 = [str_0, str_0, str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == ".\x0c.q.d.d.b.q.d.?.n.j._.k"


#@pytest.mark.xfail(strict=True)
#def test_case_1():
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_2():
    str_0 = "[+eb"
    list_0 = [str_0, str_0, str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == ".[.+.b"
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_3():
    str_0 = "f\x0bjH`it$`f%"
    list_0 = [str_0, str_0, str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == ".f.\x0b.j.h.`.t.$.`.f.%"
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_4():
    str_0 = "\x0cQdZ9dB@QyEfnv?j_7"
    list_0 = [str_0, str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == ".\x0c.q.d.z.9.d.b.@.q.f.n.v.?.j._.7"
    var_1 = module_0.func(*var_0)
    assert var_1 == ".."
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_5():
    str_0 = "*hAfA'YQc:vekQa<88<"
    list_0 = [str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == ".*.h.f.'.q.c.:.v.k.q.<.8.8.<"
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_6():
    str_0 = "o"
    list_0 = [str_0, str_0, str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == ""
    var_1 = module_0.func(*list_0)
    assert var_1 == ""
    str_1 = "5B_o 1Y.\rel$gLe"
    list_1 = [var_1, str_1]
    var_2 = module_0.func(*list_1)
    assert var_2 == ""
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_7():
    str_0 = "5|zEPVO8\\H\r"
    list_0 = [str_0, str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == ".5.|.z.p.v.8.\\.h.\r"
    list_1 = [var_0, list_0, list_0]
    var_1 = module_0.func(*list_1)
    assert var_1 == "...5...|...z...p...v...8...\\...h...\r"
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_8():
    str_0 = "|zEPV2\\H\r"
    list_0 = [str_0, str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == ".|.z.p.v.2.\\.h.\r"
    list_1 = [var_0, list_0, list_0]
    var_1 = module_0.func(*list_1)
    assert var_1 == "...|...z...p...v...2...\\...h...\r"
    str_1 = "Q())f<qJucNIO.kh"
    object_0 = module_1.object()
    var_2 = module_0.func(*var_0)
    assert var_2 == ".."
    list_2 = [str_1]
    var_3 = module_0.func(*list_2)
    assert var_3 == ".q.(.).).f.<.q.j.c.n...k.h"
    var_4 = module_0.func(*list_2)
    assert var_4 == ".q.(.).).f.<.q.j.c.n...k.h"
#    module_0.func()
