# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import possible_change as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    bool_0 = False
    var_0 = module_0.possible_change(bool_0, bool_0)
    assert var_0 == 1
    float_0 = 173.72
    module_0.possible_change(float_0, float_0)


def test_case_1():
    float_0 = -5277.557375
    var_0 = module_0.possible_change(float_0, float_0)
    assert var_0 == 0


@pytest.mark.xfail(strict=True)
def test_case_2():
    float_0 = 1315.9587
    none_type_0 = None
    var_0 = module_0.possible_change(none_type_0, float_0)
    assert var_0 == 0
    none_type_1 = None
    module_0.possible_change(float_0, none_type_1)