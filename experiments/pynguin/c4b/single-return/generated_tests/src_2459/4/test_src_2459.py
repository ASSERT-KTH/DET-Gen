# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_2459 as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_1():
    bytes_0 = b"\x04C\xc2\\~\x84;\x95)\x7fX\xc6\xd8\x8d5\x8a\xc2"
    var_0 = module_0.func(*bytes_0)
    assert var_0 == 32
    module_0.func(*var_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    bytes_0 = b"\xc7p\x8f\x93\xb9\xc5\xd3\xd2d\n\x9a\xda\xcd+/>\x87\x84\xf3"
    var_0 = module_0.func(*bytes_0)
    assert var_0 == 3
    module_0.func(*var_0)
