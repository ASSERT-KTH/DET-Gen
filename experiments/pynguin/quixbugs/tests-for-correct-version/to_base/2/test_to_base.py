# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import to_base as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    float_0 = 1157.3
    none_type_0 = None
    module_0.to_base(float_0, none_type_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    float_0 = -1620.791
    bool_0 = True
    var_0 = module_0.to_base(float_0, bool_0)
    assert var_0 == ""
    str_0 = "?C!-&\nHvWT3Rery*n\t"
    module_0.to_base(str_0, str_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    none_type_0 = None
    module_0.to_base(none_type_0, none_type_0)


@pytest.mark.xfail(strict=True)
def test_case_3():
    int_0 = 5289
    var_0 = module_0.to_base(int_0, int_0)
    assert var_0 == "10"
    none_type_0 = None
    module_0.to_base(none_type_0, none_type_0)
