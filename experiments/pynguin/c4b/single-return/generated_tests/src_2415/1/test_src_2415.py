# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_2415 as module_0


def test_case_0():
    int_0 = 2057
    list_0 = [int_0, int_0, int_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == "NO"


@pytest.mark.xfail(strict=True)
def test_case_1():
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_2():
    bytes_0 = b"\x1c\xdf\x8e"
    var_0 = module_0.func(*bytes_0)
    assert var_0 == "YES"
    module_0.func()
