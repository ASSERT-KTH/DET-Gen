# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_1453 as module_0
import builtins as module_1


#@pytest.mark.xfail(strict=True)
#def test_case_0():
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_1():
    bytes_0 = b"\xfa-\x1d\xd3@R\xd4\xf2"
    var_0 = module_0.func(*bytes_0)
    assert var_0 == 3
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_2():
    bytes_0 = b"4\xd0,\x81\xe6\x95a\xdb}\x84\x9a\x96\xdf\xc5Zw\xfa\xee\x06\x9c"
    var_0 = module_0.func(*bytes_0)
    assert var_0 == 10
    var_1 = module_1.object()
#    module_1.object(**var_1)