# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import sieve as module_0


def test_case_0():
    bool_0 = False
    var_0 = module_0.sieve(bool_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    float_0 = -1403.512
    module_0.sieve(float_0)


def test_case_2():
    int_0 = -50
    var_0 = module_0.sieve(int_0)
    bool_0 = True
    var_1 = module_0.sieve(int_0)
    int_1 = 506
    var_2 = module_0.sieve(bool_0)
    var_3 = module_0.sieve(int_1)