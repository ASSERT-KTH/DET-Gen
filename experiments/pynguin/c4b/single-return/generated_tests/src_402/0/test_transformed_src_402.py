# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_402 as module_0
import builtins as module_1


#@pytest.mark.xfail(strict=True)
#def test_case_0():
#    module_0.func()


def test_case_1():
    bytes_0 = b"\xae\x83\x0eyJ\x00<:W\xbc\x9d\x96<\x1c\x98\xb5\xc0\xa12"
    bool_0 = True
    tuple_0 = (bool_0, bytes_0, bool_0)
    var_0 = module_0.func(*tuple_0)
    assert var_0 == "NO"


def test_case_2():
    str_0 = "7"
    list_0 = [str_0, str_0, str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == "NO"


#@pytest.mark.xfail(strict=True)
def test_case_3():
    int_0 = -83
    bytes_0 = b""
    bool_0 = False
    tuple_0 = (int_0, bytes_0, bool_0)
    var_0 = module_0.func(*tuple_0)
    assert var_0 == "YES"
#    module_0.func(*var_0)


#@pytest.mark.xfail(strict=True)
def test_case_4():
    str_0 = "4"
    list_0 = [str_0, str_0, str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == "NO"
#    module_1.object(*var_0)
