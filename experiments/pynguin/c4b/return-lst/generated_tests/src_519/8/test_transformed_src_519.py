# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_519 as module_0


#@pytest.mark.xfail(strict=True)
def test_case_0():
    int_0 = 495
    list_0 = [int_0, int_0, int_0, int_0]
    var_0 = module_0.func(*list_0)
#    module_0.func(*var_0)


#@pytest.mark.xfail(strict=True)
def test_case_1():
    bool_0 = True
    list_0 = [bool_0, bool_0]
    tuple_0 = (list_0,)
    bytes_0 = b'"\xc1?)1\x82\xdb:\x0b\x9a\xd9\xa3\x81\x933c\x06\x88\x7f'
    tuple_1 = (bool_0, tuple_0, bytes_0, bytes_0)
    var_0 = module_0.func(*tuple_1)
    list_1 = []
#    module_0.func(*list_1)


#@pytest.mark.xfail(strict=True)
#def test_case_2():
#    module_0.func()
