# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_1163 as module_0


#@pytest.mark.xfail(strict=True)
def test_case_0():
    int_0 = 731
    bytes_0 = b"\xa5\x01\xb2\xb5Bb8\xe8\xdc\x11\xefZ"
    list_0 = [int_0, int_0, bytes_0]
    list_1 = [list_0, int_0, list_0, list_0]
#    module_0.func(*list_1)


#@pytest.mark.xfail(strict=True)
def test_case_1():
    none_type_0 = None
    bytes_0 = b"%m\x92\xe4q\x18\xa3\xeb\xe4\xe2\x18\x1fS\xa72w\r\xa6"
    int_0 = -3542
    int_1 = 1218
    tuple_0 = (bytes_0, int_0, int_1)
    var_0 = module_0.func(*tuple_0)
    list_0 = [none_type_0]
#    module_0.func(*list_0)


#@pytest.mark.xfail(strict=True)
#def test_case_2():
#    module_0.func()
