# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import sqrt as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    str_0 = "{{-EGn@@8kx{2#r["
    int_0 = 508
    var_0 = module_0.sqrt(int_0, int_0)
    assert var_0 == pytest.approx(25.315175154795014, abs=0.01, rel=0.01)
    module_0.sqrt(str_0, str_0)


def test_case_1():
    bool_0 = False
    var_0 = module_0.sqrt(bool_0, bool_0)
    assert var_0 == pytest.approx(0.0, abs=0.01, rel=0.01)
    var_1 = module_0.sqrt(var_0, var_0)
    var_2 = module_0.sqrt(var_1, var_0)
    bool_1 = True
    var_3 = module_0.sqrt(var_0, bool_1)
    assert var_3 == pytest.approx(0.0, abs=0.01, rel=0.01)
    var_4 = module_0.sqrt(bool_0, bool_0)
    var_5 = module_0.sqrt(var_0, var_3)


@pytest.mark.xfail(strict=True)
def test_case_2():
    complex_0 = 1442.197958 + 1631.7j
    module_0.sqrt(complex_0, complex_0)