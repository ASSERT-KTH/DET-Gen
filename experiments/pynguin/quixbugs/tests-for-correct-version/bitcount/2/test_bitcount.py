# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import bitcount as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    bytes_0 = b"ro}\xd9\xa3-pfG,T\xfa"
    module_0.bitcount(bytes_0)


def test_case_1():
    bool_0 = False
    var_0 = module_0.bitcount(bool_0)
    assert var_0 == 0
    var_1 = module_0.bitcount(bool_0)
    assert var_1 == 0


def test_case_2():
    none_type_0 = None
    var_0 = module_0.bitcount(none_type_0)
    assert var_0 == 0
    var_1 = module_0.bitcount(none_type_0)
    assert var_1 == 0
    int_0 = 274
    var_2 = module_0.bitcount(int_0)
    assert var_2 == 3
