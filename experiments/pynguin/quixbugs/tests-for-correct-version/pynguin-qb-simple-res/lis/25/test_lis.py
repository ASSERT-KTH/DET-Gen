# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import lis as module_0


def test_case_0():
    bytes_0 = b"\x99\xa0\x05\xc0\xc4"
    var_0 = module_0.lis(bytes_0)
    assert var_0 == 4


@pytest.mark.xfail(strict=True)
def test_case_1():
    float_0 = -4646.5
    list_0 = [float_0]
    list_1 = [list_0, list_0, float_0]
    module_0.lis(list_1)