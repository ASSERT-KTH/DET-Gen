# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_1946 as module_0


#@pytest.mark.xfail(strict=True)
#def test_case_0():
#    module_0.func()


def test_case_1():
    str_0 = "4c"
    list_0 = [str_0, str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == 13


def test_case_2():
    str_0 = "9e"
    list_0 = [str_0, str_0, str_0, str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == 34


def test_case_3():
    str_0 = "6e"
    list_0 = [str_0, str_0, str_0, str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == 25


#@pytest.mark.xfail(strict=True)
def test_case_4():
    str_0 = "79e"
    list_0 = [str_0, str_0, str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == 306
#    module_0.func()
