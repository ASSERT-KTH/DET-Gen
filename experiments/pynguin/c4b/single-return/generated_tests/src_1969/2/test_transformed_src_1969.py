# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_1969 as module_0


#@pytest.mark.xfail(strict=True)
#def test_case_0():
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_1():
    bytes_0 = b"\x0f\xc4>:\xd2\xa1\xf5V2Oi`[\xa6"
    var_0 = module_0.func(*bytes_0)
    assert var_0 == 21
#    module_0.func()
