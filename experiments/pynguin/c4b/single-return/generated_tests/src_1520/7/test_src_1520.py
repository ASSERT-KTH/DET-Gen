# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_1520 as module_0


def test_case_0():
    bytes_0 = b"KZ\xa8\x10Pz\xc7V\xc5\x10\x07!\x16NX\xa2"
    var_0 = module_0.func(*bytes_0)
    assert var_0 == 6


@pytest.mark.xfail(strict=True)
def test_case_1():
    module_0.func()


def test_case_2():
    bytes_0 = b"/g_\xa1\xec\xbf3"
    var_0 = module_0.func(*bytes_0)
    assert var_0 == 10
    var_1 = module_0.func(*bytes_0)
    assert var_1 == 10
