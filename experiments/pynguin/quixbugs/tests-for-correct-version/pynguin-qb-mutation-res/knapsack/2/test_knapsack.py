# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import knapsack as module_0
import builtins as module_1


@pytest.mark.xfail(strict=True)
def test_case_0():
    str_0 = "]0(*ZRoW}<Sz~nZ"
    module_0.knapsack(str_0, str_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    tuple_0 = ()
    var_0 = module_0.knapsack(tuple_0, tuple_0)
    assert var_0 == 0
    tuple_1 = (tuple_0, var_0)
    module_0.knapsack(tuple_1, tuple_1)


@pytest.mark.xfail(strict=True)
def test_case_2():
    tuple_0 = ()
    var_0 = module_0.knapsack(tuple_0, tuple_0)
    assert var_0 == 0
    tuple_1 = (tuple_0, tuple_0)
    list_0 = [tuple_1, var_0, var_0, tuple_0]
    module_0.knapsack(var_0, list_0)


@pytest.mark.xfail(strict=True)
def test_case_3():
    tuple_0 = ()
    tuple_1 = (tuple_0, tuple_0)
    bool_0 = True
    list_0 = [tuple_1, bool_0, bool_0, tuple_0]
    module_0.knapsack(bool_0, list_0)


@pytest.mark.xfail(strict=True)
def test_case_4():
    tuple_0 = ()
    var_0 = module_0.knapsack(tuple_0, tuple_0)
    assert var_0 == 0
    tuple_1 = (var_0, tuple_0)
    list_0 = [tuple_1, var_0, tuple_1, tuple_1, tuple_1, var_0, tuple_0]
    bool_0 = True
    module_0.knapsack(bool_0, list_0)


@pytest.mark.xfail(strict=True)
def test_case_5():
    int_0 = 550
    list_0 = []
    object_0 = module_1.object(*list_0)
    set_0 = {int_0, object_0}
    list_1 = [set_0, object_0, set_0]
    module_0.knapsack(int_0, list_1)