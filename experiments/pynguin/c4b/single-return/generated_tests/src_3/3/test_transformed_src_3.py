# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_3 as module_0


def test_case_0():
    bool_0 = False
    tuple_0 = ()
    list_0 = [bool_0, tuple_0, tuple_0, bool_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == 0


#@pytest.mark.xfail(strict=True)
#def test_case_1():
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_2():
    int_0 = 1412
    list_0 = [int_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == 14
#    module_0.func()
