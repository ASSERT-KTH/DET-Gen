# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_1476 as module_0
import builtins as module_1


def test_case_0():
    int_0 = 2153
    list_0 = [int_0, int_0, int_0]
    var_0 = module_0.func(*list_0)


#@pytest.mark.xfail(strict=True)
def test_case_1():
    bytes_0 = b"~_\\4\xf7-\x83\x96\x04N"
    var_0 = module_0.func(*bytes_0)
    var_1 = module_0.func(*bytes_0)
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_2():
    int_0 = -787
    bytes_0 = b"~_\\4\xf7-\x83\x96\x04N"
    list_0 = [int_0, bytes_0, int_0, bytes_0]
    var_0 = module_0.func(*list_0)
    var_1 = module_0.func(*bytes_0)
    var_2 = module_0.func(*var_0)
    var_3 = module_0.func(*var_0)
#    module_1.object(**var_2)


#@pytest.mark.xfail(strict=True)
#def test_case_3():
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_4():
    bytes_0 = b"\xf2\x0b\xcd\xb2\x9a^6<\x8a\xf7\x81\x07a\xc8n)\xdd@\x85\xb0"
    var_0 = module_0.func(*bytes_0)
    var_1 = module_0.func(*bytes_0)
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_5():
    int_0 = 2216
    list_0 = [int_0, int_0]
    var_0 = module_0.func(*list_0)
    var_1 = module_0.func(*var_0)
    list_1 = []
#    module_0.func(*list_1)
