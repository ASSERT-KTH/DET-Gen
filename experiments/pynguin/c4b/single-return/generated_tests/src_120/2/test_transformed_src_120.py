# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_120 as module_0


#@pytest.mark.xfail(strict=True)
#def test_case_0():
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_1():
    bytes_0 = b"\x89\xbbb\x03\xe3\xea\xf9\x9f\x1e\n\xb1\xcd\xe4\x82B\xbe\xf5\xe0"
    list_0 = [bytes_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == "52032"
    int_0 = 1228
#    module_0.func(*int_0)
