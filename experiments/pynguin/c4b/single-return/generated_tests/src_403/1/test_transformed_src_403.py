# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_403 as module_0


#@pytest.mark.xfail(strict=True)
#def test_case_0():
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_1():
    bytes_0 = b"\x83\x84\xfd*\x1d\xf6l6&W~\xa9"
    var_0 = module_0.func(*bytes_0)
    assert var_0 == 0
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_2():
    bytes_0 = b"\x13\x1al\xfa?\xc1\xecj\x92z\xab`g=\x19\xfe9"
    var_0 = module_0.func(*bytes_0)
    assert var_0 == 5
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_3():
    bytes_0 = b"\x83\x84*\x1dl6&W\xa9"
    var_0 = module_0.func(*bytes_0)
    assert var_0 == 5
#    module_0.func()
