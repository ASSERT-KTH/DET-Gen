# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_391 as module_0


#@pytest.mark.xfail(strict=True)
#def test_case_0():
#    module_0.func()


def test_case_1():
    bytes_0 = b"8\x97\x01\xee\x86Z\xc2o+}\x8f\xd5\x81'\n4"
    list_0 = [bytes_0, bytes_0, bytes_0, bytes_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == 3


#@pytest.mark.xfail(strict=True)
def test_case_2():
    bytes_0 = b"8\x97\x01\xee\x86Z\xc2\xd6\xb3\xf8+}\x8f\xd5\x81'\n9"
    list_0 = [bytes_0, bytes_0, bytes_0, bytes_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == 1
#    module_0.func()
