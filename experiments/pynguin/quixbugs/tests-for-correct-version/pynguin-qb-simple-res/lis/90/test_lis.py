# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import lis as module_0


def test_case_0():
    bytes_0 = b"\xfb\x0f:z4\xf0M\xfe\x82\xa9~;\xe5d\xde"
    var_0 = module_0.lis(bytes_0)
    assert var_0 == 6
    var_1 = module_0.lis(bytes_0)
    assert var_1 == 6


@pytest.mark.xfail(strict=True)
def test_case_1():
    complex_0 = 1510.6455 + 506.408046j
    module_0.lis(complex_0)


def test_case_2():
    int_0 = -2893
    list_0 = [int_0, int_0, int_0, int_0]
    var_0 = module_0.lis(list_0)
    assert var_0 == 1