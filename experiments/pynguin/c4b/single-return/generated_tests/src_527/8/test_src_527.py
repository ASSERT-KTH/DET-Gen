# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_527 as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_1():
    bytes_0 = b"\x85_\xad^2S\xee"
    var_0 = module_0.func(*bytes_0)
    assert var_0 == 0
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_2():
    bytes_0 = b"1R\x85_\xad^2S\xee"
    var_0 = module_0.func(*bytes_0)
    assert var_0 == 7
    module_0.func()
