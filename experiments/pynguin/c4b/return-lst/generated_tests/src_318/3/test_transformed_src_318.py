# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_318 as module_0


#@pytest.mark.xfail(strict=True)
def test_case_0():
    bool_0 = True
    set_0 = {bool_0, bool_0}
    var_0 = module_0.func(*set_0)
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_1():
    int_0 = 327
    list_0 = [int_0, int_0, int_0]
    var_0 = module_0.func(*list_0)
#    module_0.func()


#@pytest.mark.xfail(strict=True)
#def test_case_2():
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_3():
    bytes_0 = b"\x06\x82\xb1bR\x88v\x0b\xeeL\xa6\xf4\x04\x10\xf9\x92"
    var_0 = module_0.func(*bytes_0)
    list_0 = [bytes_0, bytes_0, bytes_0]
#    module_0.func(*list_0)
