# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_1485 as module_0
import builtins as module_1


#@pytest.mark.xfail(strict=True)
#def test_case_0():
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_1():
    bytes_0 = b"XR\x9d\xf1\xefC/\xacC[D\xc8"
    var_0 = module_0.func(*bytes_0)
    assert var_0 == 5
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_2():
    bytes_0 = b"|JR\r\xff\xf7p\xe6"
    var_0 = module_0.func(*bytes_0)
    assert var_0 == 27
#    module_1.object(*var_0)
