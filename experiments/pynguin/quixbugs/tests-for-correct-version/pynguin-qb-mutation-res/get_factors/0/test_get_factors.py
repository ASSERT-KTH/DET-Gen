# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import get_factors as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    bool_0 = True
    var_0 = module_0.get_factors(bool_0)
    dict_0 = {}
    module_0.get_factors(dict_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    none_type_0 = None
    module_0.get_factors(none_type_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    float_0 = 3490.4225
    var_0 = module_0.get_factors(float_0)
    module_0.get_factors(var_0)


@pytest.mark.xfail(strict=True)
def test_case_3():
    bool_0 = False
    var_0 = module_0.get_factors(bool_0)
    str_0 = "4a-E5$1"
    module_0.get_factors(str_0)


@pytest.mark.xfail(strict=True)
def test_case_4():
    int_0 = 2307
    none_type_0 = None
    var_0 = module_0.get_factors(int_0)
    module_0.get_factors(none_type_0)