# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import get_factors as module_0


def test_case_0():
    bool_0 = True
    var_0 = module_0.get_factors(bool_0)


#@pytest.mark.xfail(strict=True)
def test_case_1():
    list_0 = []
#    module_0.get_factors(list_0)


def test_case_2():
    bool_0 = True
    var_0 = module_0.get_factors(bool_0)
    int_0 = 403
    var_1 = module_0.get_factors(int_0)
    bool_1 = True
    var_2 = module_0.get_factors(bool_1)
