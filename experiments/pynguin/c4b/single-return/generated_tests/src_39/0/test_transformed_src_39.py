# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_39 as module_0


#@pytest.mark.xfail(strict=True)
#def test_case_0():
#    module_0.func()


def test_case_1():
    str_0 = "44"
    var_0 = module_0.func(*str_0)
    assert var_0 == "Yes"


def test_case_2():
    str_0 = "24"
    var_0 = module_0.func(*str_0)
    assert var_0 == "No"
