# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_1078 as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_1():
    bytes_0 = b"\x91\xcb\xa2Y\x83\x13\xd58\n\xb5T'm"
    var_0 = module_0.func(*bytes_0)
    assert var_0 == 1
    module_0.func()
