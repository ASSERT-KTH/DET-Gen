# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_2088 as module_0


#@pytest.mark.xfail(strict=True)
def test_case_0():
    str_0 = "9z6S]H"
    var_0 = module_0.func(*str_0)
    assert var_0 == ".9"
#    module_0.func()


#@pytest.mark.xfail(strict=True)
#def test_case_1():
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_2():
    str_0 = "\t%QE>kclgv\ruk7ykFyb@"
    list_0 = [str_0, str_0, str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == ".\t.%.q.>.k.c.l.g.v.\r.k.7.k.f.b.@"
    bool_0 = True
    list_1 = [bool_0, bool_0, bool_0]
#    module_0.func(*list_1)