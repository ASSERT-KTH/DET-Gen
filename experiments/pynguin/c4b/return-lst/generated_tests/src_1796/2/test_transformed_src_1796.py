# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_1796 as module_0
import builtins as module_1


#@pytest.mark.xfail(strict=True)
#def test_case_0():
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_1():
    int_0 = -8
    list_0 = [int_0, int_0, int_0, int_0, int_0, int_0]
    var_0 = module_0.func(*list_0)
#    module_0.func()


def test_case_2():
    bytes_0 = b"r\xc2\nb\xa5\xf3E\x1aS\x9b\x0b,\xcd\x8d"
    var_0 = module_0.func(*bytes_0)


#@pytest.mark.xfail(strict=True)
def test_case_3():
    int_0 = 1
    list_0 = [int_0, int_0, int_0, int_0]
    var_0 = module_0.func(*list_0)
    object_0 = module_1.object()
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_4():
    int_0 = 2
    list_0 = [int_0, int_0, int_0, int_0]
    var_0 = module_0.func(*list_0)
    object_0 = module_1.object()
    object_1 = module_1.object()
#    module_1.object(*var_0)


#@pytest.mark.xfail(strict=True)
def test_case_5():
    float_0 = 2319.10311
    bool_0 = True
    list_0 = [bool_0, float_0, float_0]
    var_0 = module_0.func(*list_0)
#    module_0.func(*var_0)


def test_case_6():
    bytes_0 = b"Nr\xf3E\x1aS\x9b\x0b,\xcd\x8d"
    var_0 = module_0.func(*bytes_0)
