# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_2226 as module_0


#@pytest.mark.xfail(strict=True)
def test_case_0():
    bytes_0 = b"\xcf+e\xc2\xcb\x1d*\x05\xc3\xe0\x88\xb6"
    var_0 = module_0.func(*bytes_0)
    assert var_0 == 7
#    module_0.func()


#@pytest.mark.xfail(strict=True)
#def test_case_1():
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_2():
    bytes_0 = b"SB\x98\x8d\xaaH\x9f\x9e#%:\x81u\xe6M"
    var_0 = module_0.func(*bytes_0)
    assert var_0 == 6
#    module_0.func()
