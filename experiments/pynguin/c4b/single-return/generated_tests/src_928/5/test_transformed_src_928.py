# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_928 as module_0


#@pytest.mark.xfail(strict=True)
def test_case_0():
    bytes_0 = b"\xa7\x96\xd3\xa5\r\xda\x01Wn\xdf\xebL\xb9\xfa"
    var_0 = module_0.func(*bytes_0)
    assert var_0 == 111
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_1():
    float_0 = -258.0
    list_0 = [float_0, float_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == -172
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_2():
    none_type_0 = None
#    module_0.func(*none_type_0)