# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_1942 as module_0


#@pytest.mark.xfail(strict=True)
#def test_case_0():
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_1():
    bytes_0 = b"\xe0\x96\x98\xe2\xf5\xf4\xb3\xfbj\x03J"
    var_0 = module_0.func(*bytes_0)
    assert var_0 == 4
#    module_0.func()
