# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import bitcount as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    str_0 = "X}$M;pTBE{EL"
    module_0.bitcount(str_0)


def test_case_1():
    none_type_0 = None
    var_0 = module_0.bitcount(none_type_0)
    assert var_0 == 0


@pytest.mark.xfail(strict=True)
def test_case_2():
    int_0 = 1249
    var_0 = module_0.bitcount(int_0)
    assert var_0 == 5
    int_1 = 1028
    var_1 = module_0.bitcount(int_1)
    assert var_1 == 2
    str_0 = "`_F"
    var_2 = module_0.bitcount(var_1)
    assert var_2 == 1
    module_0.bitcount(str_0)


@pytest.mark.xfail(strict=True)
def test_case_3():
    bool_0 = True
    var_0 = module_0.bitcount(bool_0)
    assert var_0 == 1
    str_0 = "f<V:Kd5"
    module_0.bitcount(str_0)