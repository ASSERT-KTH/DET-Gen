# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import gcd as module_0


#@pytest.mark.xfail(strict=True)
def test_case_0():
    int_0 = 537
    var_0 = module_0.gcd(int_0, int_0)
    assert var_0 == 537
    tuple_0 = (int_0,)
#    module_0.gcd(tuple_0, int_0)


#@pytest.mark.xfail(strict=True)
def test_case_1():
    bytes_0 = b"\xe3\x8f\xebO\xe6\xd0J\r\x04"
    none_type_0 = None
#    module_0.gcd(bytes_0, none_type_0)
