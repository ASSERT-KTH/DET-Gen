# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import sieve as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    bool_0 = True
    var_0 = module_0.sieve(bool_0)
    module_0.sieve(var_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    bytes_0 = b"'\xf4\xb3"
    module_0.sieve(bytes_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    bool_0 = True
    var_0 = module_0.sieve(bool_0)
    var_1 = module_0.sieve(bool_0)
    int_0 = 1663
    var_2 = module_0.sieve(int_0)
    var_3 = module_0.sieve(bool_0)
    var_4 = module_0.sieve(int_0)
    var_5 = module_0.sieve(int_0)
    module_0.sieve(var_1)