# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_1710 as module_0


def test_case_0():
    bool_0 = True
    list_0 = [bool_0, bool_0, bool_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == 0


#@pytest.mark.xfail(strict=True)
#def test_case_1():
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_2():
    bytes_0 = b"\xba\xb5\xfa\x02\xd4^/\xe1n9\x948l'"
    list_0 = module_0.func(*bytes_0)
    assert list_0 == 101
    dict_0 = {list_0: list_0, bytes_0: bytes_0}
    list_1 = [dict_0, bytes_0]
#    module_0.func(*list_1)
