# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_456 as module_0
import builtins as module_1


#@pytest.mark.xfail(strict=True)
#def test_case_0():
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_1():
    bytes_0 = b"g\xdf\xc2\x9b"
    list_0 = [bytes_0]
#    module_0.func(*list_0)


def test_case_2():
    str_0 = "8"
    tuple_0 = (str_0,)
    var_0 = module_0.func(*tuple_0)
    object_0 = module_1.object()


#@pytest.mark.xfail(strict=True)
def test_case_3():
    str_0 = "0"
    tuple_0 = (str_0,)
    var_0 = module_0.func(*tuple_0)
#    module_0.func()