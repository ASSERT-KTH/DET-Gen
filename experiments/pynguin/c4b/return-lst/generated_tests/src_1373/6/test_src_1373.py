# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_1373 as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    bytes_0 = b"\xdd\x10\x15@\x03V"
    module_0.func(*bytes_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_2():
    bytes_0 = b"\xc4\xc48V\xe2v\x1b"
    dict_0 = {bytes_0: bytes_0, bytes_0: bytes_0, bytes_0: bytes_0, bytes_0: bytes_0}
    list_0 = [dict_0]
    var_0 = module_0.func(*list_0)
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_3():
    int_0 = 746
    list_0 = [int_0, int_0, int_0]
    module_0.func(*list_0)
