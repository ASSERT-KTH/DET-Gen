# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_15 as module_0


def test_case_0():
    bool_0 = True
    bool_1 = True
    bool_2 = False
    list_0 = [bool_2, bool_0, bool_1, bool_2]
    list_1 = [bool_1, list_0, bool_0]
    list_2 = [bool_0, bool_0, list_1]
    var_0 = module_0.func(*list_2)


def test_case_1():
    int_0 = -2102
    list_0 = [int_0, int_0, int_0, int_0]
    var_0 = module_0.func(*list_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    int_0 = 3064
    list_0 = [int_0, int_0]
    var_0 = module_0.func(*list_0)
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_3():
    int_0 = 3041
    list_0 = [int_0, int_0, int_0, int_0]
    var_0 = module_0.func(*list_0)
    list_1 = [int_0]
    var_1 = module_0.func(*list_1)
    module_0.func()
