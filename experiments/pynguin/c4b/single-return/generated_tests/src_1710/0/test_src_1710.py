# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_1710 as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    int_0 = 6
    set_0 = {int_0}
    dict_0 = {int_0: int_0, int_0: set_0, int_0: int_0}
    var_0 = module_0.func(*dict_0)
    assert var_0 == 1
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_1():
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_2():
    bytes_0 = b"\x0cSCYH\x1d\xafM\xe6\xbd\xefw!\x82Di(\x04\xe1\r"
    var_0 = module_0.func(*bytes_0)
    assert var_0 == 3
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_3():
    bytes_0 = b"SCYH\x1d\xafM\xe6\xbd\xefw!\x82Di(\x04\xe1\r"
    var_0 = module_0.func(*bytes_0)
    assert var_0 == 43
    module_0.func()
