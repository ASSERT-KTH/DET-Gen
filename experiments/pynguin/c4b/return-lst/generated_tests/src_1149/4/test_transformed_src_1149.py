# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_1149 as module_0


#@pytest.mark.xfail(strict=True)
#def test_case_0():
#    module_0.func()


def test_case_1():
    str_0 = "5e^8!)(hff"
    var_0 = module_0.func(*str_0)


def test_case_2():
    str_0 = "5e^8!)(hff"
    int_0 = 0
    list_0 = [int_0, str_0]
    var_0 = module_0.func(*list_0)


#@pytest.mark.xfail(strict=True)
def test_case_3():
    bool_0 = True
    str_0 = "$\rjL9u)4'^A|H\x0b2qf"
    tuple_0 = (bool_0, str_0)
    var_0 = module_0.func(*tuple_0)
    str_1 = "5e^8!)(hff"
    int_0 = 0
    list_0 = [int_0, str_1]
    var_1 = module_0.func(*list_0)
#    module_0.func()
