# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_2499 as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_1():
    bytes_0 = b"8\r8"
    dict_0 = {
        bytes_0: bytes_0,
        bytes_0: bytes_0,
        bytes_0: bytes_0,
        bytes_0: bytes_0,
        bytes_0: bytes_0,
    }
    var_0 = module_0.func(*dict_0)
    assert var_0 == 1
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_2():
    bytes_0 = b"8\r88"
    dict_0 = {
        bytes_0: bytes_0,
        bytes_0: bytes_0,
        bytes_0: bytes_0,
        bytes_0: bytes_0,
        bytes_0: bytes_0,
    }
    module_0.func(*dict_0)
