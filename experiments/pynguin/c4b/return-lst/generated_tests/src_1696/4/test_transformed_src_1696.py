# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_1696 as module_0


#@pytest.mark.xfail(strict=True)
def test_case_0():
    bool_0 = False
#    module_0.func(*bool_0)


#@pytest.mark.xfail(strict=True)
def test_case_1():
    float_0 = 1001.41082
    list_0 = [float_0]
#    module_0.func(*list_0)


#@pytest.mark.xfail(strict=True)
def test_case_2():
    bytes_0 = b"L\xf03\x97\x7f\xf5/\xae\x91\x90k\xd1\xbbb"
    int_0 = 2544
    list_0 = [bytes_0, bytes_0, int_0]
    var_0 = module_0.func(*list_0)
#    module_0.func()