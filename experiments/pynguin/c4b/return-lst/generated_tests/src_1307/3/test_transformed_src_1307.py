# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_1307 as module_0


def test_case_0():
    set_0 = set()
    list_0 = [set_0, set_0, set_0, set_0]
    var_0 = module_0.func(*list_0)


#@pytest.mark.xfail(strict=True)
#def test_case_1():
#    module_0.func()


def test_case_2():
    complex_0 = -1094.55 - 3217.2564j
    set_0 = {complex_0}
    none_type_0 = None
    list_0 = [none_type_0, none_type_0]
    var_0 = module_0.func(*list_0)
    var_1 = module_0.func(*set_0)
    set_1 = set()
    list_1 = [set_1, set_1]
    var_2 = module_0.func(*list_1)


#@pytest.mark.xfail(strict=True)
def test_case_3():
    complex_0 = -1096.149777416802 - 3217.2564j
    set_0 = {complex_0}
    none_type_0 = None
    list_0 = [none_type_0, none_type_0]
    var_0 = module_0.func(*list_0)
    var_1 = module_0.func(*set_0)
#    module_0.func()


def test_case_4():
    str_0 = "UMZj"
    var_0 = module_0.func(*str_0)
    float_0 = 150.91418153140995
    dict_0 = {float_0: float_0}
    list_0 = [dict_0, var_0, dict_0, dict_0, float_0]
    var_1 = module_0.func(*list_0)
