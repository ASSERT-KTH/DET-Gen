# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import hanoi as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    bool_0 = True
    var_0 = module_0.hanoi(bool_0)
    int_0 = 524
    module_0.hanoi(int_0, var_0)


def test_case_1():
    float_0 = -3314.19
    var_0 = module_0.hanoi(float_0)
    var_1 = module_0.hanoi(float_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    none_type_0 = None
    module_0.hanoi(none_type_0, end=none_type_0)