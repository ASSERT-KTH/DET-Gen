# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_2415 as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    bytes_0 = b"\x99"
    var_0 = module_0.func(*bytes_0)
    assert var_0 == "NO"
    module_0.func()


def test_case_1():
    bytes_0 = b"\x04\xeb\xe2'ly+A\xca2\xb2y\xb3gZ\x7f"
    var_0 = module_0.func(*bytes_0)
    assert var_0 == "YES"


@pytest.mark.xfail(strict=True)
def test_case_2():
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_3():
    bytes_0 = b"\xbd\x99"
    var_0 = module_0.func(*bytes_0)
    assert var_0 == "YES"
    module_0.func()
