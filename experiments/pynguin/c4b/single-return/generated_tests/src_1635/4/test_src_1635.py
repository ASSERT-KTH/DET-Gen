# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_1635 as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    bytes_0 = b"8\x8b\xe4\xbc\xc7\xa8\xfdN2e/"
    var_0 = module_0.func(*bytes_0)
    assert var_0 == 144115188075855870
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_1():
    float_0 = -720.7
    list_0 = [float_0, float_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == 0
    list_1 = []
    module_0.func(*list_1)


@pytest.mark.xfail(strict=True)
def test_case_2():
    module_0.func()
