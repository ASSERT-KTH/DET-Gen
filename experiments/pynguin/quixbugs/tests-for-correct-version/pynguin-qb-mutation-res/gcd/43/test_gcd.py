# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import gcd as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    int_0 = 2518
    var_0 = module_0.gcd(int_0, int_0)
    assert var_0 == 2518
    var_1 = module_0.gcd(var_0, var_0)
    var_2 = module_0.gcd(int_0, int_0)
    var_3 = module_0.gcd(int_0, var_2)
    var_4 = module_0.gcd(var_3, int_0)
    none_type_0 = None
    module_0.gcd(none_type_0, none_type_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    str_0 = "GI%RN"
    module_0.gcd(str_0, str_0)