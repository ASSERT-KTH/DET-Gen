# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import lis as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    float_0 = -580.0
    str_0 = 'i${NxP]4,8(IPF+"Q'
    dict_0 = {float_0: float_0, float_0: str_0, str_0: float_0}
    module_0.lis(dict_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    str_0 = "K4aa-\x0c1v) pI]u$"
    var_0 = module_0.lis(str_0)
    assert var_0 == 5
    float_0 = -1548.0
    module_0.lis(float_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    int_0 = 250
    module_0.lis(int_0)