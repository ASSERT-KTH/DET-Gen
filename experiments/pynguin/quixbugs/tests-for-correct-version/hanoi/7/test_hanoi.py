# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import hanoi as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    float_0 = 2743.874883
    module_0.hanoi(float_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    int_0 = -3674
    var_0 = module_0.hanoi(int_0)
    module_0.hanoi(var_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    int_0 = 1966
    dict_0 = {int_0: int_0}
    module_0.hanoi(dict_0, int_0)