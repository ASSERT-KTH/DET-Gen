# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import knapsack as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    bool_0 = True
    set_0 = {bool_0}
    module_0.knapsack(set_0, set_0)


def test_case_1():
    tuple_0 = ()
    var_0 = module_0.knapsack(tuple_0, tuple_0)
    assert var_0 == 0
    var_1 = module_0.knapsack(tuple_0, tuple_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    none_type_0 = None
    module_0.knapsack(none_type_0, none_type_0)


def test_case_3():
    bool_0 = True
    tuple_0 = (bool_0, bool_0)
    list_0 = [tuple_0]
    var_0 = module_0.knapsack(bool_0, list_0)
    assert var_0 == 1


@pytest.mark.xfail(strict=True)
def test_case_4():
    bool_0 = True
    int_0 = 2270
    list_0 = [int_0, int_0]
    bytes_0 = b"\x83\xfb\x1e"
    tuple_0 = (bytes_0, list_0, bool_0)
    tuple_1 = (list_0, tuple_0)
    module_0.knapsack(bool_0, tuple_1)