# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_2545 as module_0
import builtins as module_1


#@pytest.mark.xfail(strict=True)
def test_case_0():
    bool_0 = True
    list_0 = [bool_0, bool_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == 0
#    module_0.func()


#@pytest.mark.xfail(strict=True)
#def test_case_1():
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_2():
    bytes_0 = b":H\x84"
    var_0 = module_0.func(*bytes_0)
    assert var_0 == 28
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_3():
    bytes_0 = b"\x7f\x06\x8f\x15\x1e*\xbd\xd6\x13\x03B\x99\x81\xe2\xc4\x8d\xcbs"
    var_0 = module_0.func(*bytes_0)
    assert var_0 == 63
    var_1 = module_1.object()
#    module_0.func()