# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_2312 as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    bool_0 = True
    str_0 = "QgHf-*L,Vx&@=oiJ"
    list_0 = [str_0, bool_0, str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == ".q.g.h.f.-.*.l.,.v.x.&.@.=.j"
    bool_1 = False
    list_1 = [bool_0, str_0, bool_1]
    module_0.func(*list_1)


@pytest.mark.xfail(strict=True)
def test_case_1():
    module_0.func()
