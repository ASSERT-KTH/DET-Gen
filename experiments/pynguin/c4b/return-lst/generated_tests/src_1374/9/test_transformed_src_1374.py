# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_1374 as module_0


#@pytest.mark.xfail(strict=True)
def test_case_0():
    bytes_0 = b"\xcc\x84Nv\xf6\xde\xbb\xa5&s\xc3\xfdF\x10"
    list_0 = [bytes_0, bytes_0, bytes_0]
    var_0 = module_0.func(*bytes_0)
#    module_0.func(*list_0)


#@pytest.mark.xfail(strict=True)
def test_case_1():
    bool_0 = True
    list_0 = [bool_0, bool_0, bool_0]
    var_0 = module_0.func(*list_0)
#    module_0.func()


#@pytest.mark.xfail(strict=True)
#def test_case_2():
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_3():
    bytes_0 = b"&"
    var_0 = module_0.func(*bytes_0)
#    module_0.func()
