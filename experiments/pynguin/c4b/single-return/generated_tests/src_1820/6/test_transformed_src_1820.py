# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_1820 as module_0
import builtins as module_1


#@pytest.mark.xfail(strict=True)
def test_case_0():
    bool_0 = True
    list_0 = [bool_0, bool_0, bool_0, bool_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == "NO"
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_1():
    bytes_0 = b"(;v\xd2\n\xbf\x92\xeae"
    var_0 = module_0.func(*bytes_0)
    assert var_0 == "YES"
#    module_1.object(**var_0)


#@pytest.mark.xfail(strict=True)
#def test_case_2():
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_3():
    bytes_0 = b",(a\xd2\xbf\x18e"
    bool_0 = True
    bytes_1 = b"\x8e7w\xdcN\t\xb1\x12\xeb\xcd\xa6\xe4.\xcb"
    set_0 = {bool_0, bytes_1, bool_0}
    tuple_0 = (bool_0, set_0)
    bytes_2 = b"z8\\\x12\x85j\x15\xa0'\x1c\x86\x1fW\xc1\xed\\Z\xe7"
    tuple_1 = (bool_0, bool_0, tuple_0, bytes_2)
    var_0 = module_0.func(*tuple_1)
    assert var_0 == "NO"
    var_1 = module_0.func(*bytes_0)
    assert var_1 == "YES"
#    module_0.func(*var_1)
