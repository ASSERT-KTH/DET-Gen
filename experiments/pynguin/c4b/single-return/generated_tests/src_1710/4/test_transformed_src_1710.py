# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_1710 as module_0


def test_case_0():
    bytes_0 = b"\xf5\xd3\xbf\xa5\xca>\xbe\x0e\x9fR\xa6\xbf+"
    var_0 = module_0.func(*bytes_0)
    assert var_0 == 135


#@pytest.mark.xfail(strict=True)
#def test_case_1():
#    module_0.func()
