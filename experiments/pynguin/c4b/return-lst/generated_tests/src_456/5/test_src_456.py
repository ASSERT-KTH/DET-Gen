# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_456 as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    bool_0 = False
    list_0 = [bool_0, bool_0]
    module_0.func(*list_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    bytes_0 = b"Qz\xa3\xb3\xcc)\x05\x8f\x01\x80\x9b\x84I"
    dict_0 = {bytes_0: bytes_0}
    module_0.func(*dict_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    str_0 = "2"
    var_0 = module_0.func(*str_0)
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_3():
    str_0 = "00"
    var_0 = module_0.func(*str_0)
    module_0.func()
