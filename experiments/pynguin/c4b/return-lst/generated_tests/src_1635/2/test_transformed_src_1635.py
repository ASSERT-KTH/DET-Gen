# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_1635 as module_0


#@pytest.mark.xfail(strict=True)
def test_case_0():
    int_0 = -2766
    int_1 = -2949
    list_0 = [int_0, int_0, int_0, int_1]
    var_0 = module_0.func(*list_0)
#    module_0.func(*int_0)


#@pytest.mark.xfail(strict=True)
#def test_case_1():
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_2():
    bytes_0 = b"h\xdcD2EF\x99\xb2M"
    var_0 = module_0.func(*bytes_0)
#    module_0.func()
