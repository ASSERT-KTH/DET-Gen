# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_2341 as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_1():
    bool_0 = False
    bytes_0 = b"o\xa7\xe4OM\x06\x01;\x02\xb3\x11\xad{\xea\xe9"
    tuple_0 = (bool_0, bytes_0, bytes_0, bool_0)
    var_0 = module_0.func(*tuple_0)
    assert var_0 == 0
    module_0.func(*bool_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    bool_0 = True
    bytes_0 = b""
    list_0 = [bool_0, bytes_0, bool_0]
    tuple_0 = (bool_0, bytes_0, list_0, bool_0)
    var_0 = module_0.func(*tuple_0)
    assert var_0 == 0
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_3():
    bool_0 = False
    bytes_0 = b"\x12\r\x17\x0bhAA>\xc2\xf6P\xea\xc6\xcc$,\x0f\xbe"
    list_0 = [bool_0]
    tuple_0 = (bool_0, bytes_0, list_0, bool_0)
    var_0 = module_0.func(*tuple_0)
    assert var_0 == 1
    module_0.func()