# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_1089 as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_1():
    int_0 = 320
    list_0 = [int_0, int_0, int_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == "YES\n0"
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_2():
    bytes_0 = b'\x8f\x95\x88+\x95\xe1\x11\x9a\xab\x9c\xba^+\xed"\xa1"f*'
    var_0 = module_0.func(*bytes_0)
    assert var_0 == "NO"
    module_0.func()
