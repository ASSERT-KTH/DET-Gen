# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import bitcount as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    int_0 = -1431
    module_0.bitcount(int_0)


def test_case_1():
    tuple_0 = ()
    var_0 = module_0.bitcount(tuple_0)
    assert var_0 == 0
    none_type_0 = None
    var_1 = module_0.bitcount(none_type_0)
    assert var_1 == 0
    bool_0 = False
    var_2 = module_0.bitcount(bool_0)
    assert var_2 == 0
    var_3 = module_0.bitcount(bool_0)
    assert var_3 == 0


@pytest.mark.xfail(strict=True)
def test_case_2():
    bool_0 = True
    var_0 = module_0.bitcount(bool_0)
    assert var_0 == 1
    var_1 = module_0.bitcount(var_0)
    assert var_1 == 1
    int_0 = -2613
    module_0.bitcount(int_0)