# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_2388 as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    bytes_0 = b"25d\xb4\x85W/1U\x88\xd6\xc6\xcb\x99h\xd8\xe1\xc3"
    list_0 = [bytes_0]
    module_0.func(*list_0)


def test_case_1():
    str_0 = "W#\x0bQ0.|~r0<Sk"
    dict_0 = {str_0: str_0}
    list_0 = [str_0, dict_0, dict_0, dict_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == ".w.C.+.q.P.N.|.~.r.P.\\.s.k"


@pytest.mark.xfail(strict=True)
def test_case_2():
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_3():
    str_0 = " Ka|G.lR2?,E1t1R"
    list_0 = [str_0, str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == ".@.k.|.g.N.l.r.R._.L.Q.t.Q.r"
    bool_0 = False
    list_1 = [list_0, bool_0, str_0, list_0]
    module_0.func(*list_1)
