# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import to_base as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    float_0 = 4027.963932
    module_0.to_base(float_0, float_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    int_0 = -2966
    var_0 = module_0.to_base(int_0, int_0)
    assert var_0 == ""
    module_0.to_base(var_0, var_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    none_type_0 = None
    module_0.to_base(none_type_0, none_type_0)


@pytest.mark.xfail(strict=True)
def test_case_3():
    int_0 = 380
    var_0 = module_0.to_base(int_0, int_0)
    assert var_0 == "10"
    var_1 = module_0.to_base(int_0, int_0)
    assert var_1 == "10"
    var_0.__repr__(var_1)