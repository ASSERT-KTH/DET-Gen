# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import to_base as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    float_0 = 5717.488
    bool_0 = False
    module_0.to_base(float_0, bool_0)


def test_case_1():
    int_0 = -3615
    var_0 = module_0.to_base(int_0, int_0)
    assert var_0 == ""


@pytest.mark.xfail(strict=True)
def test_case_2():
    int_0 = 169
    var_0 = module_0.to_base(int_0, int_0)
    assert var_0 == "10"
    var_0.__getitem__(var_0)