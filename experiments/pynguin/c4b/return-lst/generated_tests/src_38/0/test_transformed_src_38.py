# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_38 as module_0


def test_case_0():
    bytes_0 = b"\xbb"
    var_0 = module_0.func(*bytes_0)


#@pytest.mark.xfail(strict=True)
#def test_case_1():
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_2():
    bytes_0 = b"\x81\x8f\x16\x8e"
    int_0 = 0
    str_0 = "9'TJ;1:iRF8;o\\"
    list_0 = [int_0, int_0, str_0, bytes_0]
    var_0 = module_0.func(*list_0)
#    module_0.func()