# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_1949 as module_0


def test_case_0():
    bytes_0 = b"\xdc\xad"
    var_0 = module_0.func(*bytes_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    module_0.func()


def test_case_2():
    bytes_0 = b"BKK\xc7\xbc\x06\xabYhL?J"
    dict_0 = {bytes_0: bytes_0, bytes_0: bytes_0, bytes_0: bytes_0, bytes_0: bytes_0}
    list_0 = [dict_0, dict_0, bytes_0, bytes_0]
    var_0 = module_0.func(*list_0)


@pytest.mark.xfail(strict=True)
def test_case_3():
    str_0 = "y,e8VV "
    list_0 = [str_0, str_0, str_0]
    var_0 = module_0.func(*list_0)
    module_0.func()