# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_1534 as module_0


def test_case_0():
    str_0 = ")^}s{-\nQc>"
    var_0 = module_0.func(*str_0)
    assert var_0 == "NO"


#@pytest.mark.xfail(strict=True)
#def test_case_1():
#    module_0.func()


def test_case_2():
    str_0 = "h"
    var_0 = module_0.func(*str_0)
    assert var_0 == "NO"


def test_case_3():
    str_0 = "hcme?ClKq?.]l;h.eoK"
    list_0 = [
        str_0,
        str_0,
        str_0,
        str_0,
        str_0,
        str_0,
        str_0,
        str_0,
        str_0,
        str_0,
        str_0,
        str_0,
    ]
    var_0 = module_0.func(*list_0)
    assert var_0 == "YES"
