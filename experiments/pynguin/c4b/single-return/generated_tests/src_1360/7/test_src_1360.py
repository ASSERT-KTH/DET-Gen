# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_1360 as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    int_0 = -4795
    list_0 = [int_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == -1
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_1():
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_2():
    bytes_0 = b"\xa94"
    var_0 = module_0.func(*bytes_0)
    assert var_0 == "4477777777777777777777777"
    module_0.func()
