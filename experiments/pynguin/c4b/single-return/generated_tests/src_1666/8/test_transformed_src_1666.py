# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_1666 as module_0


def test_case_0():
    str_0 = ')iN:72"/4tW*T__2q.C;'
    var_0 = module_0.func(*str_0)
    assert var_0 == 0


#@pytest.mark.xfail(strict=True)
#def test_case_1():
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_2():
    str_0 = "9zt^>bB$M7+]v]d<KK"
    list_0 = [str_0, str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == 1
    list_1 = [str_0, str_0, list_0, list_0]
    var_1 = module_0.func(*list_1)
    assert var_1 == 1
#    module_0.func(*var_0)


#@pytest.mark.xfail(strict=True)
def test_case_3():
    str_0 = '\x0bQbT-*Pvt5f"qVV1IC'
    bool_0 = True
    list_0 = []
    tuple_0 = (str_0, bool_0, bool_0, list_0)
    var_0 = module_0.func(*tuple_0)
    assert var_0 == 1
#    module_0.func()
