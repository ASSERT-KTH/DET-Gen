# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_2294 as module_0


#@pytest.mark.xfail(strict=True)
def test_case_0():
    str_0 = "Q|zkt3ohOn-\t"
    var_0 = module_0.func(*str_0)
    assert var_0 == "YES"
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_1():
    tuple_0 = ()
    list_0 = [tuple_0, tuple_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == "NO"
    bool_0 = True
    var_1 = module_0.func(*var_0)
    assert var_1 == "NO"
    set_0 = {bool_0, bool_0, bool_0, bool_0}
#    module_0.func(*set_0)


#@pytest.mark.xfail(strict=True)
def test_case_2():
    bool_0 = False
#    module_0.func(*bool_0)
