# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_515 as module_0


def test_case_0():
    str_0 = " iDno\x0bKt-5\rW\t"
    var_0 = module_0.func(*str_0)
    assert var_0 == ". "


#@pytest.mark.xfail(strict=True)
def test_case_1():
    str_0 = " \nDno\x0bKGt-5\rW\t"
    set_0 = set()
    list_0 = [set_0, str_0, set_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == ""
    var_1 = module_0.func(*str_0)
    assert var_1 == ". "
    var_2 = module_0.func(*var_1)
    assert var_2 == ".."
#    module_0.func()


#@pytest.mark.xfail(strict=True)
#def test_case_2():
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_3():
    str_0 = " \nDno\x0bKGt-5\rW\t"
    set_0 = {str_0, str_0}
    var_0 = module_0.func(*set_0)
    assert var_0 == ". .\n.d.n.\x0b.k.g.t.-.5.\r.w.\t"
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_4():
    str_0 = "[,<O%!V\rmm{I~BvH&"
    set_0 = {str_0, str_0}
    var_0 = module_0.func(*set_0)
    assert var_0 == ".[.,.<.%.!.v.\r.m.m.{.~.b.v.h.&"
    list_0 = []
#    module_0.func(*list_0)


#@pytest.mark.xfail(strict=True)
def test_case_5():
    str_0 = "y/8k=9f\rz+#uq9}#7w2Q"
    set_0 = {str_0, str_0}
    var_0 = module_0.func(*set_0)
    assert var_0 == "./.8.k.=.9.f.\r.z.+.#.q.9.}.#.7.w.2.q"
    var_1 = module_0.func(*var_0)
    assert var_1 == ".."
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_6():
    str_0 = "[,<O\x0cE!V\rmm{I~BvH&"
    set_0 = {str_0, str_0}
    var_0 = module_0.func(*set_0)
    assert var_0 == ".[.,.<.\x0c.!.v.\r.m.m.{.~.b.v.h.&"
    list_0 = []
#    module_0.func(*list_0)


#@pytest.mark.xfail(strict=True)
def test_case_7():
    str_0 = "yA`$"
    set_0 = {str_0, str_0}
    var_0 = module_0.func(*set_0)
    assert var_0 == ".`.$"
    var_1 = module_0.func(*var_0)
    assert var_1 == ".."
#    module_0.func()
