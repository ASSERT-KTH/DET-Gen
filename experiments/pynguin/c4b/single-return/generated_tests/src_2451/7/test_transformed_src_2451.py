# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_2451 as module_0


def test_case_0():
    bool_0 = True
    tuple_0 = (bool_0, bool_0, bool_0)
    tuple_1 = (tuple_0, tuple_0)
    var_0 = module_0.func(*tuple_1)
    assert var_0 == 1


#@pytest.mark.xfail(strict=True)
#def test_case_1():
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_2():
    bool_0 = False
    tuple_0 = ()
    tuple_1 = (bool_0, tuple_0, bool_0)
    tuple_2 = (tuple_1, tuple_0)
    var_0 = module_0.func(*tuple_2)
    assert var_0 == 3
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_3():
    tuple_0 = ()
    list_0 = [tuple_0, tuple_0, tuple_0, tuple_0, tuple_0, tuple_0]
    list_1 = [list_0, tuple_0, tuple_0]
    var_0 = module_0.func(*list_1)
    assert var_0 == 2
#    module_0.func()
