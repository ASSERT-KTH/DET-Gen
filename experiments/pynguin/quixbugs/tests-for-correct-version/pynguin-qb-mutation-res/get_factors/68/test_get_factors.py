# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import get_factors as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    bool_0 = True
    var_0 = module_0.get_factors(bool_0)
    set_0 = {bool_0, bool_0}
    module_0.get_factors(set_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    dict_0 = {}
    module_0.get_factors(dict_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    int_0 = 2820
    var_0 = module_0.get_factors(int_0)
    str_0 = ":mOf\n"
    module_0.get_factors(str_0)


def test_case_3():
    bool_0 = False
    var_0 = module_0.get_factors(bool_0)