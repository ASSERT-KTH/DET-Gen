# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_779 as module_0
import builtins as module_1


#@pytest.mark.xfail(strict=True)
def test_case_0():
    bool_0 = True
    list_0 = [bool_0, bool_0, bool_0]
    var_0 = module_0.func(*list_0)
#    module_0.func()


#@pytest.mark.xfail(strict=True)
#def test_case_1():
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_2():
    bytes_0 = b"F\x1d\x18\x1a=\x01\x0c\xd1\x8b\xf6\xfa\xd5\x1fx"
    var_0 = module_0.func(*bytes_0)
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_3():
    bytes_0 = b"\x1d\x18\x1a\xc4=/\x01\xd1\x8b\xd0\xfa\x1fx"
    var_0 = module_0.func(*bytes_0)
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_4():
    bytes_0 = b"\xc6\xfb\x8cw\x97\xed\xe4\xa9\x04\xf8J\xd9"
    var_0 = module_0.func(*bytes_0)
    object_0 = module_1.object()
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_5():
    int_0 = 2026
    object_0 = module_1.object()
    list_0 = [int_0, int_0, object_0, int_0]
    var_0 = module_0.func(*list_0)
    bytes_0 = b"F\x1d\x18\x1a=\x01\xd1\x8b\xd0\xfa\xd5\x1fx"
    var_1 = module_0.func(*bytes_0)
#    module_0.func()
