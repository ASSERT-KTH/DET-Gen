# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_1949 as module_0


def test_case_0():
    bytes_0 = b"\x1a\xd5\xeaI\xb7\x85\x7f"
    var_0 = module_0.func(*bytes_0)
    assert var_0 == 0


@pytest.mark.xfail(strict=True)
def test_case_1():
    module_0.func()


def test_case_2():
    bytes_0 = b"q\xe2\xf4VV\x82(\nx^\xe5\xb1\x84c\xa5\xc6#5"
    list_0 = [bytes_0, bytes_0, bytes_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == 1


def test_case_3():
    bytes_0 = b"\x06\xce\x00\xe4KK"
    list_0 = [bytes_0, bytes_0, bytes_0, bytes_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == 1
