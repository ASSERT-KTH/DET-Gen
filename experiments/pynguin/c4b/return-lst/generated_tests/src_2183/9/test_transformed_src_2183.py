# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_2183 as module_0


def test_case_0():
    bool_0 = True
    tuple_0 = (bool_0, bool_0, bool_0)
    list_0 = [bool_0, tuple_0, bool_0]
    var_0 = module_0.func(*list_0)


#@pytest.mark.xfail(strict=True)
#def test_case_1():
#    module_0.func()


def test_case_2():
    bool_0 = False
    list_0 = [bool_0, bool_0]
    var_0 = module_0.func(*list_0)


def test_case_3():
    bool_0 = True
    str_0 = "7=<~{H"
    dict_0 = {
        bool_0: bool_0,
        bool_0: bool_0,
        str_0: bool_0,
        str_0: bool_0,
        bool_0: bool_0,
        bool_0: bool_0,
    }
    var_0 = module_0.func(*dict_0)


#@pytest.mark.xfail(strict=True)
def test_case_4():
    str_0 = "7pcv\x0bH"
    float_0 = 125.0
    list_0 = [float_0, str_0]
#    module_0.func(*list_0)


def test_case_5():
    bool_0 = True
    str_0 = "4"
    dict_0 = {
        bool_0: bool_0,
        bool_0: bool_0,
        str_0: bool_0,
        bool_0: bool_0,
        bool_0: str_0,
        bool_0: bool_0,
        bool_0: str_0,
        bool_0: bool_0,
    }
    var_0 = module_0.func(*dict_0)
