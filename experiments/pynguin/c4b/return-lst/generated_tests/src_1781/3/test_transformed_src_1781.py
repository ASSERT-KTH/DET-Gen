# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_1781 as module_0


#@pytest.mark.xfail(strict=True)
def test_case_0():
    bool_0 = True
    tuple_0 = ()
    tuple_1 = (tuple_0,)
    list_0 = [bool_0, tuple_1]
    var_0 = module_0.func(*list_0)
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_1():
    bool_0 = False
    list_0 = [bool_0, bool_0]
    var_0 = module_0.func(*list_0)
    bytes_0 = b"\xd0\xebj"
#    module_0.func(*bytes_0)


#@pytest.mark.xfail(strict=True)
#def test_case_2():
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_3():
    int_0 = 4060
    set_0 = {int_0, int_0, int_0, int_0}
#    module_0.func(*set_0)
