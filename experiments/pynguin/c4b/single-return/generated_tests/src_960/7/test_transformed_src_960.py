# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_960 as module_0


def test_case_0():
    bool_0 = False
    list_0 = [bool_0]
    var_0 = module_0.func(*list_0)


#@pytest.mark.xfail(strict=True)
#def test_case_1():
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_2():
    bytes_0 = b"\xdf\xfc\xd1\xba$\x04\x03\xd5\xf0\xba"
    var_0 = module_0.func(*bytes_0)
#    module_0.func()


def test_case_3():
    bool_0 = True
    list_0 = [bool_0]
    var_0 = module_0.func(*list_0)
    var_1 = module_0.func(*list_0)
