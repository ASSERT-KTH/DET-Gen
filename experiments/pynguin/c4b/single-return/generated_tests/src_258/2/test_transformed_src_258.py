# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_258 as module_0


#@pytest.mark.xfail(strict=True)
#def test_case_0():
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_1():
    bytes_0 = b"\xeaV_\x11\xa6\x8e\x0b\xac\xf9%\xda"
    var_0 = module_0.func(*bytes_0)
    assert var_0 == 11
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_2():
    bytes_0 = b"\x0e\xe2\x0e4\x96\xdc\x92\xf2\x16s\x02\xbe\xce?\xcf\x19\x8f\xd3["
    var_0 = module_0.func(*bytes_0)
    assert var_0 == 12
#    module_0.func()
