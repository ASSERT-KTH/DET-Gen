# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_2335 as module_0


#@pytest.mark.xfail(strict=True)
#def test_case_0():
#    module_0.func()


def test_case_1():
    str_0 = "}LqR&"
    bytes_0 = b""
    tuple_0 = (bytes_0,)
    int_0 = 2529
    tuple_1 = (str_0, str_0, tuple_0, int_0)
    var_0 = module_0.func(*tuple_1)
    assert var_0 == ".}.l.q.r.&"
    var_1 = module_0.func(*tuple_0)
    assert var_1 == ""


def test_case_2():
    bytes_0 = b""
    tuple_0 = (bytes_0,)
    var_0 = module_0.func(*tuple_0)
    assert var_0 == ""
    var_1 = module_0.func(*tuple_0)
    assert var_1 == ""


#@pytest.mark.xfail(strict=True)
def test_case_3():
    str_0 = "`syzuyf]wGB9mezq-Q"
    list_0 = [str_0, str_0, str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == ".`.s.z.f.].w.g.b.9.m.z.q.-.q"
    bytes_0 = b""
    tuple_0 = (bytes_0,)
    int_0 = 2529
    tuple_1 = (str_0, str_0, tuple_0, int_0)
    var_1 = module_0.func(*tuple_1)
    assert var_1 == ".`.s.z.f.].w.g.b.9.m.z.q.-.q"
#    module_0.func()
