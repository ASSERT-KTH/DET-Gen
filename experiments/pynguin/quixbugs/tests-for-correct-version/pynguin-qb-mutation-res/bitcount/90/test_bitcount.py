# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import builtins as module_0
import bitcount as module_1


@pytest.mark.xfail(strict=True)
def test_case_0():
    object_0 = module_0.object()
    module_1.bitcount(object_0)


def test_case_1():
    none_type_0 = None
    var_0 = module_1.bitcount(none_type_0)
    assert var_0 == 0


@pytest.mark.xfail(strict=True)
def test_case_2():
    int_0 = -2224
    module_1.bitcount(int_0)


@pytest.mark.xfail(strict=True)
def test_case_3():
    bool_0 = True
    var_0 = module_1.bitcount(bool_0)
    assert var_0 == 1
    object_0 = module_0.object()
    module_1.bitcount(object_0)