# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_1537 as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    str_0 = "*q]VOu.k1?hF1F`& ;!"
    bool_0 = False
    tuple_0 = (str_0, bool_0)
    var_0 = module_0.func(*tuple_0)
    assert var_0 == ".*.q.].v...k.1.?.h.f.1.f.`.&. .;.!"
    var_1 = module_0.func(*var_0)
    assert var_1 == ".."
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_1():
    tuple_0 = ()
    list_0 = [tuple_0, tuple_0, tuple_0, tuple_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == ""
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_2():
    module_0.func()
