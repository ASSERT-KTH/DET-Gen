# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import gcd as module_0


def test_case_0():
    bool_0 = False
    var_0 = module_0.gcd(bool_0, bool_0)
    assert var_0 is False


@pytest.mark.xfail(strict=True)
def test_case_1():
    str_0 = "EZki*n2o.q"
    module_0.gcd(str_0, str_0)
