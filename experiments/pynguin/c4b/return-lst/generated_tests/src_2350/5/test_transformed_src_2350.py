# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_2350 as module_0


def test_case_0():
    bool_0 = True
    list_0 = [bool_0, bool_0]
    var_0 = module_0.func(*list_0)


#@pytest.mark.xfail(strict=True)
def test_case_1():
    bytes_0 = b"+\x00\x86i\xb7\x0b&.\x95\x98\xd5\xdb1D\xe8D\xee\xde"
    list_0 = [bytes_0]
    var_0 = module_0.func(*list_0)
    none_type_0 = None
#    module_0.func(*none_type_0)


#@pytest.mark.xfail(strict=True)
#def test_case_2():
#    module_0.func()
