# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_1895 as module_0


def test_case_0():
    str_0 = "2\nq<4,WP=3sa"
    var_0 = module_0.func(*str_0)


#@pytest.mark.xfail(strict=True)
#def test_case_1():
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_2():
    int_0 = -4360
    list_0 = [int_0, int_0]
    list_1 = [list_0]
#    module_0.func(*list_1)


def test_case_3():
    str_0 = "2\nq<4,WP=3sa"
    var_0 = module_0.func(*str_0)
    list_0 = [var_0]
    var_1 = module_0.func(*list_0)


#@pytest.mark.xfail(strict=True)
def test_case_4():
    str_0 = "0xUKjY?\x0b_f'@-"
    var_0 = module_0.func(*str_0)
#    module_0.func()
