# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import get_factors as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    bool_0 = True
    var_0 = module_0.get_factors(bool_0)
    module_0.get_factors(var_0)


def test_case_1():
    int_0 = 2817
    var_0 = module_0.get_factors(int_0)
