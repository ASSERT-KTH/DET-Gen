# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import knapsack as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    str_0 = "FHl<y}"
    str_1 = "y]"
    module_0.knapsack(str_1, str_0)


def test_case_1():
    tuple_0 = ()
    var_0 = module_0.knapsack(tuple_0, tuple_0)
    assert var_0 == 0


@pytest.mark.xfail(strict=True)
def test_case_2():
    int_0 = -825
    module_0.knapsack(int_0, int_0)


@pytest.mark.xfail(strict=True)
def test_case_3():
    bool_0 = True
    int_0 = -1926
    dict_0 = {bool_0: int_0, int_0: int_0}
    tuple_0 = (dict_0, int_0, bool_0)
    module_0.knapsack(bool_0, tuple_0)


@pytest.mark.xfail(strict=True)
def test_case_4():
    bool_0 = True
    int_0 = 1463
    dict_0 = {int_0: int_0, bool_0: int_0, int_0: int_0}
    tuple_0 = (dict_0, int_0, bool_0)
    module_0.knapsack(bool_0, tuple_0)