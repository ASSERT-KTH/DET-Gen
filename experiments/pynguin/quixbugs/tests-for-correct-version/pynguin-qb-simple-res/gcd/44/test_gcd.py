# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import gcd as module_0


def test_case_0():
    bool_0 = False
    var_0 = module_0.gcd(bool_0, bool_0)
    assert var_0 is False


def test_case_1():
    int_0 = -2056
    var_0 = module_0.gcd(int_0, int_0)
    assert var_0 == -2056