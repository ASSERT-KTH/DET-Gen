# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_2294 as module_0


#@pytest.mark.xfail(strict=True)
def test_case_0():
    str_0 = "#$wS88kJ2|b5h"
    var_0 = module_0.func(*str_0)
    assert var_0 == "NO"
    var_1 = module_0.func(*str_0)
    assert var_1 == "NO"
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_1():
    bool_0 = False
#    module_0.func(*bool_0)


#@pytest.mark.xfail(strict=True)
def test_case_2():
    str_0 = "^@p2^dQa7"
    list_0 = [str_0, str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == "YES"
#    module_0.func()
