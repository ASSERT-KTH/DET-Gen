# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_1580 as module_0


def test_case_0():
    int_0 = -4464
    list_0 = [int_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == ""


def test_case_1():
    int_0 = -4447
    list_0 = [int_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == "7"


@pytest.mark.xfail(strict=True)
def test_case_2():
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_3():
    int_0 = 3
    dict_0 = {int_0: int_0, int_0: int_0}
    int_1 = 337
    tuple_0 = (dict_0, int_0, int_1, dict_0)
    tuple_1 = ()
    list_0 = [tuple_0, tuple_1]
    list_1 = [int_0, list_0]
    var_0 = module_0.func(*list_1)
    assert var_0 == "7"
    module_0.func()
