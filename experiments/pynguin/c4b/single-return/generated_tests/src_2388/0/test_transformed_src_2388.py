# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_2388 as module_0


#@pytest.mark.xfail(strict=True)
def test_case_0():
    bool_0 = True
    list_0 = [bool_0, bool_0, bool_0, bool_0]
    list_1 = [list_0]
#    module_0.func(*list_1)


def test_case_1():
    str_0 = ", P\x0c]-=Om1\r4wBv"
    str_1 = "1"
    list_0 = [str_1, str_0, str_1]
    var_0 = module_0.func(*list_0)
    assert var_0 == ".Q"
    list_1 = [str_0, str_0, str_1, str_1]
    var_1 = module_0.func(*list_1)
    assert var_1 == ".L.@.p.,.}.M.].m.Q.-.T.w.b.v"


#@pytest.mark.xfail(strict=True)
#def test_case_2():
#    module_0.func()
