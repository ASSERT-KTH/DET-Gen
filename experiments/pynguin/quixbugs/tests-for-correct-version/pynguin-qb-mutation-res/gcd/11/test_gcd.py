# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import gcd as module_0


def test_case_0():
    bool_0 = False
    set_0 = {bool_0, bool_0}
    var_0 = module_0.gcd(set_0, bool_0)
    bool_1 = False
    var_1 = module_0.gcd(bool_1, bool_1)
    var_2 = module_0.gcd(bool_1, bool_1)


@pytest.mark.xfail(strict=True)
def test_case_1():
    dict_0 = {}
    module_0.gcd(dict_0, dict_0)