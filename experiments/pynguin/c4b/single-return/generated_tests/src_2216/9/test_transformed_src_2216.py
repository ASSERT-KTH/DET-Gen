# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_2216 as module_0
import builtins as module_1


#@pytest.mark.xfail(strict=True)
#def test_case_0():
#    module_0.func()


def test_case_1():
    str_0 = "4\r5"
    tuple_0 = (str_0, str_0)
    var_0 = module_0.func(*tuple_0)
    assert var_0 == 1


#@pytest.mark.xfail(strict=True)
def test_case_2():
    bool_0 = False
    str_0 = "14\r5"
    bytes_0 = b"IS\x92\xdbiT@\xde\x9e'\xc2\xd59\x88]\x01H\x83"
    tuple_0 = (str_0, bytes_0)
    var_0 = module_0.func(*tuple_0)
    assert var_0 == 0
#    module_0.func(*bool_0)


#@pytest.mark.xfail(strict=True)
def test_case_3():
    bool_0 = False
    str_0 = "4\r6"
    bytes_0 = b"IS\x92\xdbiT@\xde\x9e'\xc2\xd59\x88]\x01H\x83"
    tuple_0 = (str_0, bytes_0)
    var_0 = module_0.func(*tuple_0)
    assert var_0 == 2
    object_0 = module_1.object()
#    module_1.object(**bool_0)
