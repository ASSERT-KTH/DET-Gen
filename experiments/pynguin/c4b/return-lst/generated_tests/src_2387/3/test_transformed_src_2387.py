# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_2387 as module_0


def test_case_0():
    str_0 = "m;{2"
    list_0 = [str_0]
    var_0 = module_0.func(*list_0)


def test_case_1():
    str_0 = "@[z1\x0b&!pV"
    var_0 = module_0.func(*str_0)


#@pytest.mark.xfail(strict=True)
#def test_case_2():
#    module_0.func()


def test_case_3():
    bool_0 = True
    tuple_0 = (bool_0, bool_0, bool_0, bool_0)
    list_0 = [tuple_0, bool_0, bool_0]
    var_0 = module_0.func(*list_0)


def test_case_4():
    bool_0 = True
    tuple_0 = (bool_0, bool_0, bool_0, bool_0)
    list_0 = [
        tuple_0,
        tuple_0,
        tuple_0,
        bool_0,
        bool_0,
        bool_0,
        bool_0,
        bool_0,
        tuple_0,
    ]
    list_1 = [list_0, list_0, bool_0, tuple_0]
    var_0 = module_0.func(*list_1)


#@pytest.mark.xfail(strict=True)
def test_case_5():
    bool_0 = False
    tuple_0 = (bool_0, bool_0, bool_0, bool_0)
    list_0 = [
        tuple_0,
        tuple_0,
        tuple_0,
        bool_0,
        bool_0,
        bool_0,
        bool_0,
        bool_0,
        bool_0,
        bool_0,
        tuple_0,
    ]
    list_1 = [list_0, list_0, bool_0, tuple_0]
    var_0 = module_0.func(*list_0)
    var_1 = module_0.func(*list_1)
#    module_0.func()
