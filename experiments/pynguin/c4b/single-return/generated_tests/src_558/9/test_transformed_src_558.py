# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_558 as module_0


#@pytest.mark.xfail(strict=True)
def test_case_0():
    bytes_0 = b"k\xd1\xdaWpu"
    var_0 = module_0.func(*bytes_0)
    assert var_0 == 2
#    module_0.func()


#@pytest.mark.xfail(strict=True)
#def test_case_1():
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_2():
    bytes_0 = b"\x83*\x13\x18B\xed3\xb3\xe6\xcf\x8f\x08\xde\xbd\x84\xb3\xd9\x0b\xbe\xac"
    var_0 = module_0.func(*bytes_0)
    assert var_0 == 6
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_3():
    bytes_0 = b"k\xd1\xdaW\x00pu"
    var_0 = module_0.func(*bytes_0)
    assert var_0 == 0
#    module_0.func()
