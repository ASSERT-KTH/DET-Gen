# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import bitcount as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    int_0 = -1611
    module_0.bitcount(int_0)


def test_case_1():
    tuple_0 = ()
    var_0 = module_0.bitcount(tuple_0)
    assert var_0 == 0


def test_case_2():
    bool_0 = True
    var_0 = module_0.bitcount(bool_0)
    assert var_0 == 1