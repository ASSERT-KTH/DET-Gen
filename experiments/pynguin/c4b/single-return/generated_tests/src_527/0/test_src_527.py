# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_527 as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_1():
    bytes_0 = b"<\x0e1pr\x9f\x0f~\x07\x98\x8d\xe2C\xbb\xcd"
    var_0 = module_0.func(*bytes_0)
    assert var_0 == 10
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_2():
    bytes_0 = b"<\xda\x0e1p\x05\x9f\x0f~\x07\x98\x8d\x07C\xeb\xcd"
    var_0 = module_0.func(*bytes_0)
    assert var_0 == 10
    list_0 = [bytes_0]
    module_0.func(*list_0)
