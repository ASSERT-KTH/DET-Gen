# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_2183 as module_0


#@pytest.mark.xfail(strict=True)
#def test_case_0():
#    module_0.func()


def test_case_1():
    str_0 = "65"
    var_0 = module_0.func(*str_0)


def test_case_2():
    int_0 = -1099
    list_0 = [int_0, int_0, int_0]
    var_0 = module_0.func(*list_0)


#@pytest.mark.xfail(strict=True)
def test_case_3():
    str_0 = '74Ubp+b"'
#    module_0.func(*str_0)


#@pytest.mark.xfail(strict=True)
def test_case_4():
    bool_0 = False
    set_0 = {bool_0, bool_0, bool_0}
    tuple_0 = (bool_0, set_0, bool_0)
    list_0 = [bool_0, tuple_0, set_0, set_0]
    var_0 = module_0.func(*list_0)
    str_0 = '97UbpSb"'
#    module_0.func(*str_0)


#@pytest.mark.xfail(strict=True)
def test_case_5():
    bool_0 = False
    list_0 = [bool_0, bool_0]
    var_0 = module_0.func(*list_0)
    bool_1 = True
    set_0 = {bool_1, bool_1, bool_1}
    tuple_0 = (bool_1, set_0, bool_1)
    list_1 = [bool_1, tuple_0, set_0, set_0]
    var_1 = module_0.func(*list_1)
    str_0 = "17Vu%&~."
    var_2 = module_0.func(*str_0)
#    module_0.func()
