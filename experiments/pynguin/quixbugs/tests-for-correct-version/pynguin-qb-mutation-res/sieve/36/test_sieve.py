# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import sieve as module_0
import builtins as module_1


@pytest.mark.xfail(strict=True)
def test_case_0():
    int_0 = 1380
    var_0 = module_0.sieve(int_0)
    none_type_0 = None
    module_0.sieve(none_type_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    int_0 = -679
    var_0 = module_0.sieve(int_0)
    module_0.sieve(var_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    object_0 = module_1.object()
    module_0.sieve(object_0)