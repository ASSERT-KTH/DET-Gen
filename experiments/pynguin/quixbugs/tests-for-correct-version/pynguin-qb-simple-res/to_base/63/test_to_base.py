# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import to_base as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    int_0 = 1491
    var_0 = module_0.to_base(int_0, int_0)
    assert var_0 == "10"
    bool_0 = False
    var_0.setdefault(var_0, bool_0)


def test_case_1():
    float_0 = -565.5
    var_0 = module_0.to_base(float_0, float_0)
    assert var_0 == ""