# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import gcd as module_0


def test_case_0():
    int_0 = -4482
    int_1 = 2079
    var_0 = module_0.gcd(int_0, int_1)
    assert var_0 == 27


@pytest.mark.xfail(strict=True)
def test_case_1():
    none_type_0 = None
    module_0.gcd(none_type_0, none_type_0)