# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_2147 as module_0
import builtins as module_1


#@pytest.mark.xfail(strict=True)
def test_case_0():
    int_0 = -4452
    float_0 = -509.837213
    list_0 = [int_0, int_0, float_0, float_0, int_0]
    var_0 = module_0.func(*list_0)
#    module_0.func()


#@pytest.mark.xfail(strict=True)
#def test_case_1():
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_2():
    bytes_0 = b"q\x91\xc3%|\xf0\xcc\xf2\xce\xa6\xcd\xbc\xdd"
    var_0 = module_0.func(*bytes_0)
    object_0 = module_1.object()
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_3():
    bool_0 = False
    list_0 = [bool_0, bool_0, bool_0, bool_0]
    var_0 = module_0.func(*list_0)
    bytes_0 = b"\x06\x9d)3\xb2f*"
    var_1 = module_0.func(*bytes_0)
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_4():
    bool_0 = False
    list_0 = [bool_0, bool_0, bool_0, bool_0]
    var_0 = module_0.func(*list_0)
    object_0 = module_1.object()
    var_1 = module_0.func(*var_0)
    var_2 = module_1.object()
#    module_0.func()
