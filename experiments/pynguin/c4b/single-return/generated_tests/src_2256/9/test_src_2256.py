# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_2256 as module_0
import builtins as module_1


@pytest.mark.xfail(strict=True)
def test_case_0():
    bytes_0 = b"\xff\x94Rh"
    tuple_0 = (bytes_0,)
    list_0 = [tuple_0, tuple_0]
    module_0.func(*list_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    str_0 = "Gt+0MZ\x0bA\r"
    var_0 = module_0.func(*str_0)
    assert var_0 == ".g"
    list_0 = [str_0, str_0, str_0, str_0]
    list_1 = [list_0, var_0, var_0]
    var_1 = module_0.func(*list_1)
    assert var_1 == ""
    module_0.func(*var_1)


@pytest.mark.xfail(strict=True)
def test_case_2():
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_3():
    str_0 = "Np71Q$wHkvC"
    list_0 = [str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == ".n.p.q.w.h.k.v.c"
    object_0 = module_1.object()
    module_0.func()
