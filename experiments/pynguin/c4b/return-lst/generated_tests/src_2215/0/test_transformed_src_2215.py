# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_2215 as module_0


#@pytest.mark.xfail(strict=True)
def test_case_0():
    bytes_0 = b"6\xa0\x16\xfb\xee\xf7\x12D\x1c8\xe9~"
    list_0 = [bytes_0, bytes_0, bytes_0, bytes_0]
    var_0 = module_0.func(*list_0)
#    module_0.func()


#@pytest.mark.xfail(strict=True)
#def test_case_1():
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_2():
    bytes_0 = b"6\xa0\x16\xfb\xee\xf7\x12D\x1c8\xe9~"
    list_0 = [bytes_0, bytes_0, bytes_0, bytes_0]
    tuple_0 = module_0.func(*list_0)
    var_0 = module_0.func(*tuple_0)
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_3():
    bytes_0 = b"\xfe"
    list_0 = [bytes_0, bytes_0]
    var_0 = module_0.func(*list_0)
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_4():
    bytes_0 = b"\x8f3\x90\xc9_\xad\x0f$\x90@\xc3"
    list_0 = [bytes_0, bytes_0, bytes_0, bytes_0]
    var_0 = module_0.func(*list_0)
    var_1 = module_0.func(*var_0)
#    module_0.func()