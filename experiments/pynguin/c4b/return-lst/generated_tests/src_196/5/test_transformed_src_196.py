# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_196 as module_0


#@pytest.mark.xfail(strict=True)
#def test_case_0():
#    module_0.func()


def test_case_1():
    str_0 = "M>2 I$\r$x6k<Y\n "
    var_0 = module_0.func(*str_0)


def test_case_2():
    str_0 = "M>2 I$\r$x6k<Y\n "
    var_0 = module_0.func(*str_0)
    var_1 = module_0.func(*str_0)
    var_2 = module_0.func(*var_1)


#@pytest.mark.xfail(strict=True)
def test_case_3():
    str_0 = 'UO\\%TH!.\n`4Dm" '
    list_0 = [str_0]
#    module_0.func(*list_0)


#@pytest.mark.xfail(strict=True)
def test_case_4():
    str_0 = "!$OS]"
    var_0 = module_0.func(*str_0)
    var_1 = module_0.func(*var_0)
    var_2 = module_0.func(*str_0)
    var_3 = module_0.func(*var_2)
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_5():
    str_0 = "z!S]0hujFG"
    int_0 = -188
    tuple_0 = (str_0, int_0)
#    module_0.func(*tuple_0)
