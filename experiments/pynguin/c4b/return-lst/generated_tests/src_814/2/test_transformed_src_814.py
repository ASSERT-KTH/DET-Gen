# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_814 as module_0


def test_case_0():
    int_0 = -15
    dict_0 = {int_0: int_0, int_0: int_0}
    tuple_0 = (dict_0, int_0)
    list_0 = [int_0, int_0, tuple_0, tuple_0]
    var_0 = module_0.func(*list_0)


#@pytest.mark.xfail(strict=True)
#def test_case_1():
#    module_0.func()


def test_case_2():
    int_0 = -15
    dict_0 = {int_0: int_0, int_0: int_0}
    tuple_0 = (dict_0, int_0)
    list_0 = [int_0, int_0, tuple_0, tuple_0]
    var_0 = module_0.func(*list_0)
    var_1 = module_0.func(*var_0)


def test_case_3():
    int_0 = 1
    dict_0 = {int_0: int_0, int_0: int_0}
    tuple_0 = (dict_0,)
    str_0 = "f2M4_ku\x0b/$4c&"
    tuple_1 = (dict_0, str_0)
    list_0 = [int_0, int_0, tuple_0, tuple_1]
    var_0 = module_0.func(*list_0)


def test_case_4():
    int_0 = -4
    dict_0 = {int_0: int_0, int_0: int_0}
    tuple_0 = (dict_0, int_0)
    list_0 = [int_0, int_0, tuple_0, tuple_0]
    var_0 = module_0.func(*list_0)
