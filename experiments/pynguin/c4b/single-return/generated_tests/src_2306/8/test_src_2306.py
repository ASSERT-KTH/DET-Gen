# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_2306 as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_1():
    set_0 = set()
    int_0 = 317
    list_0 = [int_0, int_0, int_0, int_0, int_0, set_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == 1
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_2():
    bytes_0 = b'\x03"\xfa\x0e\xedn\xf2\xed\x19f\x0f\x97\xed'
    var_0 = module_0.func(*bytes_0)
    assert var_0 == 94
    set_0 = set()
    int_0 = 317
    list_0 = [int_0, int_0, int_0, int_0, int_0, set_0]
    var_1 = module_0.func(*list_0)
    assert var_1 == 1
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_3():
    bytes_0 = b'\x03"\xdd\x0b\xfa\x0e\xedn\xf2\xed\x19f\x0f\x97\xed'
    var_0 = module_0.func(*bytes_0)
    assert var_0 == 104
    module_0.func(*var_0)
