# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_258 as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_1():
    bytes_0 = b"\x0f\x910:\xec\xd5u!9\x83\xba\xfc\xcc_Q"
    var_0 = module_0.func(*bytes_0)
    assert var_0 == 24
    module_0.func()
