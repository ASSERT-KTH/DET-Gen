# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_2458 as module_0


def test_case_0():
    bytes_0 = b"\x07\xdd\xe3I+\xa5\xfb\x95\xdbq\xf1\x0b\xc0"
    var_0 = module_0.func(*bytes_0)
    assert var_0 == 6


@pytest.mark.xfail(strict=True)
def test_case_1():
    module_0.func()


def test_case_2():
    bytes_0 = b"\x10\x0e\xb8\x057\xa2\x9f:\xf4\x88^\x0b<\xb1uH|\x0b"
    var_0 = module_0.func(*bytes_0)
    assert var_0 == 17


def test_case_3():
    bytes_0 = b"\xbd\xca\x8f\xd9\xf3\x0f\xd3"
    var_0 = module_0.func(*bytes_0)
    assert var_0 == 4
