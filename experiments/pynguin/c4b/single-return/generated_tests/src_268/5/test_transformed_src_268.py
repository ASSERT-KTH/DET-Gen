# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_268 as module_0


def test_case_0():
    str_0 = "C/%"
    tuple_0 = (str_0,)
    var_0 = module_0.func(*tuple_0)
    assert var_0 == 0


#@pytest.mark.xfail(strict=True)
#def test_case_1():
#    module_0.func()


def test_case_2():
    str_0 = 'QVV\nM"gG'
    tuple_0 = (str_0,)
    var_0 = module_0.func(*tuple_0)
    assert var_0 == 1
