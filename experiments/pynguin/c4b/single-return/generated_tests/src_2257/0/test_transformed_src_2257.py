# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_2257 as module_0


#@pytest.mark.xfail(strict=True)
def test_case_0():
    str_0 = ";*Ps`z\x0c0]:wpD"
    var_0 = module_0.func(*str_0)
    assert var_0 == ";"
#    module_0.func()


#@pytest.mark.xfail(strict=True)
#def test_case_1():
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_2():
    str_0 = ";*Ps`z\x0c0]:wpD"
    tuple_0 = (str_0,)
    var_0 = module_0.func(*tuple_0)
    assert var_0 == ";*Ps`z\x0c0]:wpD"
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_3():
    str_0 = "A\rR48~<+\r"
    var_0 = module_0.func(*str_0)
    assert var_0 == "a"
    tuple_0 = (str_0,)
    var_1 = module_0.func(*tuple_0)
    assert var_1 == "a\rr48~<+\r"
#    module_0.func()
