# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import sqrt as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    int_0 = 207
    var_0 = module_0.sqrt(int_0, int_0)
    assert var_0 == pytest.approx(17.821000162443127, abs=0.01, rel=0.01)
    var_1 = module_0.sqrt(int_0, int_0)
    assert var_1 == pytest.approx(17.821000162443127, abs=0.01, rel=0.01)
    str_0 = "j"
    module_0.sqrt(str_0, var_0)


def test_case_1():
    bool_0 = False
    var_0 = module_0.sqrt(bool_0, bool_0)
    assert var_0 == pytest.approx(0.0, abs=0.01, rel=0.01)
    var_1 = module_0.sqrt(bool_0, bool_0)
    float_0 = 2152.1849
    var_2 = module_0.sqrt(var_0, float_0)
    assert var_2 == pytest.approx(0.0, abs=0.01, rel=0.01)
    int_0 = 1562
    var_3 = module_0.sqrt(int_0, int_0)
    assert var_3 == pytest.approx(42.739119022760676, abs=0.01, rel=0.01)
    var_4 = module_0.sqrt(int_0, int_0)
    assert var_4 == pytest.approx(42.739119022760676, abs=0.01, rel=0.01)
    var_5 = module_0.sqrt(var_0, int_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    complex_0 = -285.2 - 3668.021946j
    module_0.sqrt(complex_0, complex_0)
