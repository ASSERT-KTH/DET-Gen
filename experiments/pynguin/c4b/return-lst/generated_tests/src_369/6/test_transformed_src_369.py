# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_369 as module_0


def test_case_0():
    str_0 = ";EYHK"
    var_0 = module_0.func(*str_0)


#@pytest.mark.xfail(strict=True)
#def test_case_1():
#    module_0.func()


def test_case_2():
    str_0 = ";EYHK"
    var_0 = module_0.func(*str_0)
    var_1 = module_0.func(*var_0)


#@pytest.mark.xfail(strict=True)
def test_case_3():
    str_0 = ""
    list_0 = [str_0, str_0]
    var_0 = module_0.func(*list_0)
#    module_0.func()


def test_case_4():
    float_0 = 4214.2943
    tuple_0 = (float_0,)
    list_0 = [float_0, tuple_0]
    str_0 = ";EYHK"
    tuple_1 = (tuple_0, float_0, str_0)
    var_0 = module_0.func(*tuple_1)
    bool_0 = True
    list_1 = [str_0, bool_0, list_0]
    var_1 = module_0.func(*list_1)