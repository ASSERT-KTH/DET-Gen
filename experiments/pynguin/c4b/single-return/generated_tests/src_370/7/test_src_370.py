# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_370 as module_0
import builtins as module_1


def test_case_0():
    bytes_0 = b"\xeb\x8a\x9d\xb8&h\xb8\x14Y\xe4\xcaR\x1b\x9cV4"
    var_0 = module_0.func(*bytes_0)
    assert var_0 == 0


@pytest.mark.xfail(strict=True)
def test_case_1():
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_2():
    bytes_0 = b"F\xa9\xa1z\xa3\x1f'\xf2\xd8\xce"
    var_0 = module_0.func(*bytes_0)
    assert var_0 == 4
    module_1.object(**var_0)


def test_case_3():
    bytes_0 = b'\xac"*\xd1n-S'
    var_0 = module_0.func(*bytes_0)
    assert var_0 == 5


def test_case_4():
    bytes_0 = b"\xeb\x9d\xb8&h\xb8\x14Y\xcaR\x1b\x9cV4"
    var_0 = module_0.func(*bytes_0)
    assert var_0 == 2


@pytest.mark.xfail(strict=True)
def test_case_5():
    bytes_0 = b"\xfd\xff~\xb5\x00\xe5\\\xef\xf8)\x84\xfc\xfc\xb8\n\xc8\x1c"
    var_0 = module_0.func(*bytes_0)
    assert var_0 == 0
    module_1.object(**var_0)
