# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_194 as module_0


#@pytest.mark.xfail(strict=True)
def test_case_0():
    set_0 = set()
    str_0 = "V"
    bool_0 = False
    tuple_0 = (set_0, str_0, bool_0)
    list_0 = [tuple_0, set_0, tuple_0]
#    module_0.func(*list_0)


#@pytest.mark.xfail(strict=True)
def test_case_1():
    int_0 = -2221
    list_0 = [int_0, int_0, int_0, int_0]
#    module_0.func(*list_0)


#@pytest.mark.xfail(strict=True)
#def test_case_2():
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_3():
    set_0 = set()
    str_0 = "V"
    bool_0 = False
    tuple_0 = (set_0, str_0, bool_0)
    list_0 = [tuple_0, set_0, tuple_0]
    var_0 = module_0.func(*str_0)
    assert var_0 == "V"
#    module_0.func(*list_0)
