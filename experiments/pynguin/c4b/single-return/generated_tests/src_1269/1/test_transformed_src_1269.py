# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_1269 as module_0


#@pytest.mark.xfail(strict=True)
#def test_case_0():
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_1():
    bytes_0 = b"3\t'\x86; o\x07"
    int_0 = 130
    list_0 = [int_0, bytes_0, int_0, int_0]
#    module_0.func(*list_0)


#@pytest.mark.xfail(strict=True)
def test_case_2():
    bytes_0 = b"m\xbdZ\xf8ra`\xe5\x8f\n\n\xf1\xe4\xef\x06\xdc\x8bs\x11\xcb"
    int_0 = -149
    set_0 = {bytes_0, bytes_0, int_0}
    var_0 = module_0.func(*set_0)
    assert var_0 == 7
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_3():
    bytes_0 = b"3\t'\x86; o\xdf\x07"
    int_0 = 1
    list_0 = [int_0, bytes_0, int_0, int_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == 1
#    module_0.func()
